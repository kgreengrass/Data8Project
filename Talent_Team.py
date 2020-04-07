from files_to_dataframe import FileToDF
from sklearn.preprocessing import LabelEncoder
import pandas as pd


def talentteammatcher():  # this function generates a table which is suitable for doing the merge based on name
    file= FileToDF('data8-engineering-project', 'Talent')
    df = file.dataframecsv()
    df = df[['invited_by']]
    df = df.dropna(axis=0)
    df = df.replace('Bruno Belbrook', 'Bruno Bellbrook')
    df = df.replace('Fifi Etton', 'Fifi Eton')
    df = df.drop_duplicates()
    talent_le = LabelEncoder()
    df['Talent_Team_ID'] = talent_le.fit_transform(df['invited_by'])
    df['Talent_Team_ID'] += 1
    return df

def talentteamtable():  ## this function generates the table which is ready to be inputted into sql
    df = talentteammatcher()
    first_last_names = df['invited_by'].str.split(" ", 1, expand=True)
    first_last_names.columns =['first_name','last_name']
    df = pd.concat([df, first_last_names], axis=1)
    df= df.drop(['invited_by'], axis=1)
    return df
