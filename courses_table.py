import boto3
import pandas as pd
from course_types import course_types
from Courses import dateformat
from Courses import dataframe
from Trainers import trainers

def courses_table():
    df = dateformat('Start_Date')
    types = course_types()
    trainer_match = trainers()
    df = pd.merge(df,types ,on="Course Type")
    df = pd.merge(df, trainer_match, on="trainer")
    df = df.drop(['Course Type', 'trainer'], axis=1)
    return df
