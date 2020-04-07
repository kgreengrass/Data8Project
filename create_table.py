from files_to_dataframe import FileToDF
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from json_reader import ReadTransformJson
import numpy as np


class Table:

    def __init__(self, bucket, bucket_folder):
        self.bucket = bucket
        self.bucket_folder = bucket_folder


    # def import_table(self):
    #
    #
    #
    # def transform_table(self):
    #
    #
    #
    # def export_table(self):


class TrainerTable(Table):

    def __init__(self):


    def trainers(): # for matching IDs with
        file= FileToDF('data8-engineering-project', 'Academy')
        df = file.dataframecsv()
        df = df[['trainer']]
        df = df.drop_duplicates()
        name_le = LabelEncoder()
        df['TrainerID'] = name_le.fit_transform(df['trainer'])
        df['TrainerID'] += 1
        return df



    def trainerstable(): # finalised table for sql
        df = trainers()
        first_last_names = df['trainer'].str.split(" ", 1, expand=True)
        first_last_names.columns =['first_name','last_name']
        df = pd.concat([df, first_last_names], axis=1)
        df = df.drop(['trainer'], axis=1)
        return df

    def strengths():
        strength_list= extract('strengths')
        df = pd.DataFrame(strength_list)
        df.columns=['StrengthName']
        df['StrengthID'] = np.arange(len(df))
        return df


    def weaknesses():
        weakness_list = extract('weaknesses')
        df = pd.DataFrame(weakness_list)
        df.columns=['WeaknessName']
        df['WeaknessID'] = np.arange(len(df))
        return df


    def extract(y):
        file = FileToDF('data8-engineering-project', 'TransformedFiles')
        df = file.dataframecsv()
        list1 = []
        for row in df[y]:
            chars = ["'", "[", "]"]
            for c in chars:
                row = row.replace(c, '')
            row = row.split(',')
            for x in row:
                x = x.strip()
                if x not in list1:
                    list1.append(x)
        return list1


    def tech():
        file = ReadTransformJson('data8-engineering-project', 'Interview Notes')
        df = file.json_reader('Interview Notes') # uses json reader so can access technologies as a dictionary but will take longer to run
        tech_list = []
        for row in df.technologies:
            for tech in row:
                tech = tech['language']
                if tech not in tech_list:
                    tech_list.append(tech)
        df = pd.DataFrame(tech_list)
        df.columns=['TechName']
        df['TechID'] = np.arange(len(df))
        return df


    def academiestable():
        file= FileToDF('data8-engineering-project', 'SpartaDays')
        df = file.dataframetxt()
        df = df[['academy']]
        academy_le = LabelEncoder()
        df['AcademyID'] = academy_le.fit_transform(df['academy'])
        df = df.drop_duplicates()
        df['AcademyID'] += 1
        return df