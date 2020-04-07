from files_to_dataframe import FileToDF
from sklearn.preprocessing import LabelEncoder
import pandas as pd

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
