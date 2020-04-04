import boto3
from pprint import pprint
import csv
import pandas as pd

s3_client = boto3.client('s3')
contents = s3_client.list_objects_v2(Bucket='data8-engineering-project')['Contents']
for x in contents:
    splitfile = x['Key'].split('/')
    if splitfile[0] == 'Academy':   ###doesnt work because all the taqlent ones are more than 1000th in the list
        data = s3_client.get_object(Bucket='data8-engineering-project',
                                    Key = x['Key'])
        df = pd.read_csv(data['Body'])

print(df)
