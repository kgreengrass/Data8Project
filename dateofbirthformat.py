import pandas as pd
from files_to_dataframe import FileToDF

def dateformat(bucket, folder, col):   # takes in the bucket and folder and creates df & formats column specified to date
    file = FileToDF(bucket, folder)
    df = FileToDF.dataframecsv(file)
    df[col] = pd.to_datetime(df[col])
    return df
