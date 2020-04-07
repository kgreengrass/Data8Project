from files_to_dataframe import FileToDF
from sklearn.preprocessing import LabelEncoder

def academiestable():
    file= FileToDF('data8-engineering-project', 'SpartaDays')
    df = file.dataframetxt()
    df = df[['academy']]
    academy_le = LabelEncoder()
    df['AcademyID'] = academy_le.fit_transform(df['academy'])
    df = df.drop_duplicates()
    df['AcademyID'] += 1
    return df
