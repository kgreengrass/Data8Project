from dateofbirthformat import dateformat
import pandas as pd
from datetime import datetime

def test_dateformat():
    df_test = dateformat('data8-engineering-project','Test_talent', 'dob')

    date1 = datetime.strptime('1994-04-08', '%Y-%m-%d')
    df_date1 = pd.DataFrame({'dob': [date1]})

   # asert df_test.equals(df_result)
    df_result = pd.DataFrame({'id': [1],
                              'name': ['Esme Trusslove'],
                              'gender': ['Female'],
                              'dob': [date1],
                              'email': ['etrusslove0@google.es'],
                              'city': ['Swindon'],
                              'address': ['22056 Lerdahl Avenue'],
                              'postcode': ['SN1'],
                              'phone_number': [-1262],
                              'uni': ["Saint George's Hospital Medical School, University of London"],
                              'degree': ['02:01'],
                              'invited_date': [10],
                              'month': ['Apr-19'],
                              'invited_by': ['Bruno Bellbrook']
                              })

    assert df_test.equals(df_result)




