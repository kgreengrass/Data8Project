from strength_weakness_tech import strengths
from strength_weakness_tech import weaknesses
import link_files
import pandas as pd

def candidate_strengths():  # returns dataframe with candidate id and strength id
    df = candidate_extract('strengths')
    df.columns = ['CandidateID', 'StrengthName']
    df = pd.merge(df, strengths(), on='StrengthName')  # merges to get the strength IDs
    df.drop('StrengthName', axis=1, inplace=True)
    return df

def candidate_weaknesses():  # returns dataframe of candidate id and weakness id
    df = candidate_extract('weaknesses')
    df.columns = ['CandidateID', 'WeaknessName']
    df = pd.merge(df, weaknesses(), on='WeaknessName')  # merges to get the weakness IDs
    df.drop('WeaknessName', axis=1, inplace=True)
    return df

def candidate_extract(z):
    df = link_files.merge('TransformedFiles')
    df = df[['CandidateID', z]]
    list = []
    for index, row in df.iterrows():
        x = row[z]
        chars = ["'", "[", "]"]
        for c in chars:
            x = x.replace(c, '')
        row[z] = x.split(',')  # breaks down what looks like a list but is a string into an actual list
        for x in row[z]:
            x = x.strip()
            y = row['CandidateID']
            list.append([y, x])  # appends each individual strength with it's matching candidate ID to a list
    df = pd.DataFrame(list)
    return df

