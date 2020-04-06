import boto3
import pandas as pd
from datetime import datetime


def dataframetxt(bucket, folder):
    s3_client = boto3.client('s3')
    contents = s3_client.list_objects_v2(Bucket=bucket, Prefix=f'{folder}/')['Contents']
    df_list =[]
    for x in contents:
        splitkey = x['Key'].split('.')
        if splitkey[-1] == 'txt':  # checks its a .txt file
            data = s3_client.get_object(Bucket=bucket,
                                        Key = x['Key'])
            file = data['Body']
            df1 = pd.read_csv(file,sep="\t", header=None, skiprows=3)  # gets psychometrics and presentation marks for each name
            file.close()  #Have to  close and reassign file to read from it again to get date and academy
            data = s3_client.get_object(Bucket=bucket,
                                        Key=x['Key'])
            file = data['Body']
            dateacdf = pd.read_csv(file,sep="\t", header=None, skiprows=lambda x: x not in [0,1]) # gets the date and academy
            date = dateacdf.iloc[0][0]  # gets the date (which is in row 1 of dataframe created)
            date = datetime.strptime(date, "%A %d %B %Y")  # formats date
            academy = dateacdf.iloc[1][0]  # gets the academy name (second row of dataframe created)
            academy = academy.split(' ')[0]  # gets just the location name (takes out the word academy)
            df1['date'] = date
            df1['academy'] = academy
            splitdf = df1[0].str.rsplit("-", 1, expand=True)  # splits full name from everything else (splits on last - so '-' in names don't affect it)
            scoredf = splitdf[1].str.split("/|:|,", expand=True)  # splits all the stats up score, max.score, name of assessment
            name_list=[]
            for index, row in splitdf.iterrows():  # goes through each row of the file being uploaded
                row[0]=row[0].strip()  # strips any whitespace off beginning and end
                if row[0].count(' ') == 1:  # checks to see if only the one space
                    name_list.append(row[0].split(" ", 1))  # automatically splits name into first and last and adds to list
                else:
                    name_list.append(inputspace(row[0]))  # adds the name from the manually choosing space to split function
            namedf = pd.DataFrame(name_list)  # creates a dataframe from the name list created above
            fulldf = pd.concat([namedf, scoredf, df1['academy'], df1['date']], axis=1) # concatenates all the formatted created above so all columns are correct
            df_list.append(fulldf) # adds the dataframe for this file to a list
        else:
            pass
    df = pd.concat(df_list) # creates one dataframe for all the files that have been processed above
    df.columns = ["first_name","last_name",'col1','psychometrics','psycho.max','col2','presentation','present.max','academy','date']
    df.drop(['col1','col2'], axis=1, inplace=True)
    df[['psychometrics','psycho.max','presentation','present.max']]=df[['psychometrics','psycho.max','presentation',
                                                                        'present.max']].apply(pd.to_numeric)
    return df


def inputspace(row):  # function for asking for user input for where the space should be
    while True:  # checks input is a number and in range of number of spaces
        try:
            space = int(input(f'{row} \n '  # asks for input on where to split the name
                          f'Please input number for the space that separates first and last name i.e. '
                          f'input 1 for 1st space, 2 for 2nd space etc.: '))
            if 1 <= space <= row.count(' '):
                splits = row.split(' ')  # splits by all spaces
                # creates the name as a list, joining the relevant number splits to give the correct first and second name:
                name = [' '.join(splits[:space]), ' '.join(splits[space:])]
                return name
        except (ValueError, TypeError):  # won't pass the try if the string can't be changed into an integer
            pass





