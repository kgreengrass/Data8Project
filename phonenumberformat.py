import boto3
import pandas as pd
import numpy as np

def dataframe(bucket, folder):
    s3_client = boto3.client('s3')
    contents = s3_client.list_objects_v2(Bucket=bucket, Prefix=f'{folder}/')['Contents']
    df_list =[]
    for x in contents:
        splitkey = x['Key'].split('.')
        if splitkey[-1] == 'csv':
            data = s3_client.get_object(Bucket='data8-engineering-project',
                                        Key = x['Key'])
            df1 = pd.read_csv(data['Body'])
            df_list.append(df1)
        else:
            pass
    df = pd.concat(df_list)
    return df

def phonenoformat(bucket, folder, col):
    df = dataframe(bucket, folder)
    df[col]=df[col].astype(str)
    chars = ' ()-'
    for c in chars:
        df[col] = df[col].str.replace(c,'')
    df.replace('nan', np.nan, inplace=True)
    return df

print(phonenoformat('data8-engineering-project', 'Talent','phone_number').phone_number)