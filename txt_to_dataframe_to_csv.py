import pandas as pd
from datetime import datetime

def txt_df_csv(file_name):
    # takes a txt file, creates a data frame, adds columns: date and academy (row 1 and 2 in a file, respectively)

    # gets data starting from 4th row, 3rd row is blank
    data = pd.read_csv(file_name,
                       sep=";|/|:|,|-",
                       header=None,
                       skiprows=3,
                       engine='python')

    # gets data about date and Academy name
    extradata = pd.read_csv(file_name,
                            header=None,
                            skiprows=lambda x: x not in [0, 1])

    date = extradata.iloc[0][0]
    date = datetime.strptime(date, "%A %d %B %Y")
    academy = extradata.iloc[1][0]
    academy = academy.split(' ')[0]

    # adds Date and Academy columns
    data['Date'] = date
    data['Academy'] = academy

    # splits name into first_name and last_name columns
    first_last_names = data[0].str.split(" ", 1, expand=True)
    first_last_names.columns = ['first_name', 'last_name']
    data.columns = ['name', 'col1', 'psychometrics', 'psycho. max', 'col4', 'presentation', 'present. max', 'date',
                    'academy']

    # create the final data frame
    df = pd.concat([data, first_last_names], axis=1)
    df.drop('col1', axis=1, inplace=True)
    df.drop('col4', axis=1, inplace=True)

    # save file in csv format
    df.to_csv('txtpandas2csv.csv', index=False)



txt_df_csv('Sparta Day 1 August 2019.txt')