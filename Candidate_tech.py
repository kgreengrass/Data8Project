from strength_weakness_tech import tech
import link_files
from json_reader import ReadTransformJson
import pandas as pd


def candidate_tech():
    file = ReadTransformJson('data8-engineering-project', 'Interview Notes')
    df = file.json_reader('Interview Notes')  # uses json reader so can access technologies as a dictionary but will take longer to run
    df = df[['name', 'technologies']] # takes just the columns name and technologies
    list1 = []
    for index, row in df.iterrows():  # goes through each row of dataframe
        technology = row['technologies']  # assigns the technologies column to a variable
        for x in technology:  # goes through the list of dictionaries in the technologies column
            techno = x['language']  # take the language name
            score = x['self_score']  # takes the language score
            name = row['name']  # takes the candidate name for this row of dataframe
            list1.append([name, techno, score])  # append the language name, score and the candidate name
    df = pd.DataFrame(list1)  # creates dataframe from the list created above
    df.columns = ['name', 'TechName', 'self_score']  # renames columns to use for merging
    df = pd.merge(df, tech(), on='TechName')  # merges to get the tech IDs
    df = link_files.namecon(df)  # uses function to create the name column without special characters
    df = pd.merge(df,link_files.talentfile()[['CandidateID', 'namecon']], on = 'namecon' )  # merges the candidateID on
    df.drop(['TechName', 'namecon', 'name'], axis=1, inplace=True) # drops unneeded columns
    return df

print(candidate_tech())