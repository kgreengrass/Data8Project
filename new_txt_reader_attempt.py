import boto3
import pandas as pd
from pprint import pprint

def files(bucket, *folders):
    s3 = boto3.resource('s3')
    data_bucket = s3.Bucket(bucket)
    contents = data_bucket.objects.all()
    filenames = {}
    for x in contents:
        folder = x.key.split('/')[0]
        file = x.key.split('/')[1]
        if folder not in folders:
            pass
        elif folder in filenames:
            filenames[folder].append(file)
        else:
            filenames[folder] = [file]

    return filenames
info = files('data8-engineering-project', 'SpartaDays' )
s3_client = boto3.client('s3')
for x in info.values():
    for y in range(0,len(x)):
        name = x[y] # gets the individual files names
        data = s3_client.get_object(Bucket='data8-engineering-project',
                                            Key = 'SpartaDays/' + name)
        df1 = pd.read_csv(data['Body'], sep=" ", header=None)
        df1



############
####ANNA'S TXT TRANSFORMER
# import pandas as pd
# from datetime import datetime
#
# data = pd.read_csv('Sparta Day 1 May 2019.txt', sep=" ", header=None, skiprows=3)
# print(data)
# # gets data starting from 4th row, 1st row is date, 2nd row is name of Academy
# data = pd.read_csv('Sparta Day 1 May 2019.txt',
#                    sep=";|/|:|,|-",
#                    header=None,
#                    skiprows=3,
#                    engine='python')
#
# # gets data about date and Academy name
# extradata = pd.read_csv('Sparta Day 1 August 2019.txt',
#                         header=None,
#                         skiprows=lambda x: x not in [0,1])
#
# date = extradata.iloc[0][0]
#
# academy = extradata.iloc[1][0]
# print(academy)
# date = datetime.strptime(date, "%A %d %B %Y")
#
# academy = academy.split(' ')[0]
# data['Date'] = date
# data['Academy'] = academy
#
# data.columns = ['name', 'col1', 'psychometrics', 'psycho. max', 'col4', 'presentation', 'present. max', 'date', 'academy']
# data2 = data[['name', 'psychometrics', 'psycho. max', 'presentation', 'present. max', 'date', 'academy']]
#
# first_last_names = data2['name'].str.split(" ", 1, expand=True)
# first_last_names.columns =['first_name','last_name']
#
# df = pd.concat([data2, first_last_names], axis=1)