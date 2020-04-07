from files_to_dataframe import FileToDF
import pandas as pd
from json_reader import ReadTransformJson
import numpy as np


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

