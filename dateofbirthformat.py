import boto3
import pandas as pd

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

def dateformat(bucket, folder, col):   # takes in the bucket and folder and creates df using above function & formats column specified to date
    df = dataframe(bucket, folder)
    df[col] = pd.to_datetime(df[col])
    return df

