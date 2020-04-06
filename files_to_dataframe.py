import boto3
import pandas as pd
from datetime import datetime
from FileDictionary import files

class FileToDF:

    def __init__(self, bucket, folder):
        self.folder = folder
        self.bucket = bucket
        self.file_names_dict = files(bucket, folder)
        self.s3_client = boto3.client('s3')

    def filenames(self):
        content_list = []
        for index, record in enumerate(self.file_names_dict[self.folder]):
            contents = self.s3_client.list_objects_v2(Bucket=self.bucket,
                                            Prefix=f'{self.folder}/{record}')['Contents']
            content_list.append(contents)  # creates a list of all files in folder (even if over 1000)
        return content_list


    def dataframecsv(self):
        contents = self.filenames()
        df_list =[]
        for x in contents:
            for y in x:
                splitkey = y['Key'].split('.')
                if splitkey[-1] == 'csv':
                    data = self.s3_client.get_object(Bucket=self.bucket,
                                                Key = y['Key'])
                    df1 = pd.read_csv(data['Body'])
                    df_list.append(df1)
                else:
                    pass
        df = pd.concat(df_list)
        return df

    def dataframetxt(self):
        contents = self.filenames()
        df_list = []
        for x in contents:
            for y in x:
                splitkey = y['Key'].split('.')
                if splitkey[-1] == 'txt':  # checks its a .txt file
                    data = self.s3_client.get_object(Bucket=self.bucket,
                                                Key=y['Key'])
                    file = data['Body']
                    df1 = pd.read_csv(file, sep="\t", header=None,
                                      skiprows=3)  # gets psychometrics and presentation marks for each name
                    file.close()  # Have to  close and reassign file to read from it again to get date and academy
                    data = self.s3_client.get_object(Bucket=self.bucket,
                                                Key=y['Key'])
                    file = data['Body']
                    dateacdf = pd.read_csv(file, sep="\t", header=None,
                                           skiprows=lambda x: x not in [0, 1])  # gets the date and academy
                    date = dateacdf.iloc[0][0]  # gets the date (which is in row 1 of dataframe created)
                    date = datetime.strptime(date, "%A %d %B %Y")  # formats date
                    academy = dateacdf.iloc[1][0]  # gets the academy name (second row of dataframe created)
                    academy = academy.split(' ')[0]  # gets just the location name (takes out the word academy)
                    df1['date'] = date
                    df1['academy'] = academy
                    splitdf = df1[0].str.rsplit("-", 1,
                                                expand=True)  # splits full name from everything else (splits on last - so '-' in names don't affect it)
                    scoredf = splitdf[1].str.split("/|:|,",
                                                   expand=True)  # splits all the stats up score, max.score, name of assessment
                    fulldf = pd.concat([splitdf[0], scoredf, df1['academy'], df1['date']],
                                       axis=1)  # concatenates all the formatted created above so all columns are correct
                    df_list.append(fulldf)  # adds the dataframe for this file to a list
                else:
                    pass
        df = pd.concat(df_list)  # creates one dataframe for all the files that have been processed above
        df.columns = ["name", 'col1', 'psychometrics', 'psycho.max', 'col2', 'presentation', 'present.max',
                      'academy', 'date']
        df.drop(['col1', 'col2'], axis=1, inplace=True)
        df[['psychometrics', 'psycho.max', 'presentation', 'present.max']] = df[
            ['psychometrics', 'psycho.max', 'presentation',
             'present.max']].apply(pd.to_numeric)
        return df

