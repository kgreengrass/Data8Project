import link_files
import pandas as pd
from AcademiesTable import academiestable
from course_types import course_types

def interviewnotes():
    df1 = link_files.merge('TransformedFiles')
    df2 = link_files.merge('SpartaDays')
    df3= pd.merge(df1[['CandidateID', 'geo_flex', 'self_development', 'financial_support_self','result', 'course_interest']],
                 df2[['CandidateID', 'academy', 'psychometrics', 'presentation','date']], on='CandidateID')
    df3.rename(columns={'course_interest': 'Course Type'}, inplace=True)
    df4 = pd.merge(df3, academiestable(), on ='academy')
    df = pd.merge(df4, course_types(), on = 'Course Type')
    df.drop(['Course Type', 'academy'],axis =1, inplace = True)
    return df

print(interviewnotes().dtypes)