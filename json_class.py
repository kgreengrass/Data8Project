import boto3
from pprint import pprint
import json
import pandas as pd
from FileDictionary import files

# For the interview notes bucket it may take 5 min to write into the df
class ReadTransformJson:
    """
    A class that will import json files from s3 and load them into a pandas dataframe
    """

    def __init__(self, bucket, bucket_folder):
        self.bucket = bucket
        self.bucket_folder = bucket_folder
        self.main_df = ''  # this is a place holder
        self.file_names_dict = files(bucket, bucket_folder)

    def json_reader(self):
        s3_client = boto3.client('s3')
        for index, record in enumerate(self.file_names_dict[self.bucket_folder]):
            column_list = []  # will be keys of dict
            value_list = []  # will be values of dict
            s3object = s3_client.get_object(Bucket=self.bucket,
                                            Key=self.bucket_folder + '/' + record)
            bson_dict_file = s3object['Body'].read()  # reads in binary
            json_dict_file = json.loads(bson_dict_file)
            for key in json_dict_file:  # extract the keys for column names
                column_list.append(key)
            for value in json_dict_file.values():  # extract the values to insert as rows
                value_list.append(value)
            df = self.create_df(value_list, column_list)  # creating a panda df
            if index == 0:  # this is provisional; needs to be first file
                self.main_df = df
            else:
                self.append_df(df)  # append to the first created dataframe
        return self.main_df

    def structure_json(self):
        # iterate through all the keys and get the values and insert in the dataframe
        pass

    def create_df(self, row, column):
        df = pd.DataFrame([row], columns=column)
        return df

    def append_df(self, df):
        self.main_df = self.main_df.append(df, ignore_index=True)


if __name__ == '__main__':
    test_instance = ReadTransformJson('data8-engineering-project', 'Interview Notes')
    interview_notes_df = test_instance.json_reader()
    # interview_notes_df.to_csv('interview_notes1.csv')
