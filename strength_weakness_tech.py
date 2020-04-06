from files_to_dataframe import FileToDF
import pandas as pd

def strengths():
    file = FileToDF('data8-engineering-project', 'TransformedFiles')
    df = file.dataframecsv()
    strength_list = []
    chars = ["'","[", "]"]
    for row in df.strengths:
        for c in chars:
            row = row.replace(c,'')
        row = row.split(',')
        for strength in row:
            strength = strength.strip()
            if strength not in strength_list:
                strength_list.append(strength)

    df = pd.DataFrame(strength_list)
    return df


def weaknesses():
    file = FileToDF('data8-engineering-project', 'TransformedFiles')
    df = file.dataframecsv()
    weakness_list = []
    chars = ["'", "[", "]"]
    for row in df.weaknesses:
        for c in chars:
            row = row.replace(c, '')
        row = row.split(',')
        for weakness in row:
            weakness = weakness.strip()
            if weakness not in weakness_list:
                weakness_list.append(weakness)

    df = pd.DataFrame(weakness_list)
    return df

