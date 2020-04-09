from link_files import talentfile
from link_files import merge
import boto3
import pandas as pd
from Talent_Team import talentteammatcher
from split_name_auto import splitname
from link_files import namecon



def coursecand():
    bucket = 'data8-engineering-project'
    folder = 'Academy'
    s3_client = boto3.client('s3')
    contents = s3_client.list_objects_v2(Bucket=bucket, Prefix=f'{folder}/')['Contents']
    df_list = []
    for x in contents:
        splitkey = x['Key'].split('.')
        if splitkey[-1] == 'csv':
            data = s3_client.get_object(Bucket='data8-engineering-project',
                                        Key=x['Key'])
            df1 = pd.read_csv(data['Body'])
            name = x['Key'].split('/')[1] ####finds the name of the file
            course_type = name.split('_')[0]##splits the file up and takes the first part of it i.e. 'business', 'data'
            course_initial = course_type[0]
            course_number = name.split('_')[1]  ####takes the second entry, i.e. a number
            conc = course_initial + course_number ####concatenates the course type and the number of which group it is
            df1['CourseID'] = conc  # creates an extra column in the dataframe called course that contains the concatenated course name
            df2 = df1[['CourseID', 'name']]
            df_list.append(df2)
        else:
            pass
        df = pd.concat(df_list)
    return df


def phonenoformat(df, col):
    df = df
    df[col] = df[col].astype(str)
    chars = ' ()-'
    for c in chars:
        df[col] = df[col].str.replace(c, '')
    return df

def dateformat(df,
               col):  # takes in the bucket and folder and creates df using above function & formats column specified to date
    df = df
    df[col] = pd.to_datetime(df[col])
    return df

def candidates_table():
    df=talentfile()
    df = phonenoformat(df, 'phone_number')
    df = dateformat(df, 'dob')
    cc = namecon(coursecand())
    cc = cc.drop(['name'], axis=1)
    df = pd.merge(df, cc, how='left', on= 'namecon')
    df = df.replace('Bruno Belbrook', 'Bruno Bellbrook')
    df = df.replace('Fifi Etton', 'Fifi Eton')
    TT = talentteammatcher()
    df = pd.merge(df, TT, how='left', on='invited_by')
    df1 = splitname(df['name'])
    df1.columns = ['first_name', 'last_name']
    df =  pd.concat([df, df1], axis=1)
    df = df.drop(['namecon', 'id', 'invited_by', 'invited_date', 'month', 'name'], axis=1)
    df = df.fillna(0)
    return df
