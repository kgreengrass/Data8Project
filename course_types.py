from files_to_dataframe import FileToDF
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from Courses import dateformat
from Courses import dataframe


def course_types():  # for matching IDs with
    df = dateformat('Start_Date')
    df = df[['Course Type']]
    df = df.drop_duplicates()
    type_le = LabelEncoder()
    df['course_type_ID'] = type_le.fit_transform(df['Course Type'])
    df['course_type_ID'] += 1
    return df

