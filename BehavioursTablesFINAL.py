import boto3
import pandas as pd
from files_to_dataframe import FileToDF
from sklearn.preprocessing import LabelEncoder
from link_files import namecon
from link_files import talentfile

def dataframe(bucket, folder):
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
            course_type = name.split('_')[0] ##splits the file up and takes the first part of it i.e. 'business', 'data'
            course_number = name.split('_')[1]  ####takes the second entry, i.e. a number
            conc = course_type + ' ' + course_number ####concatenates the course type and the number of which group it is
            course_start = name.split('_')[2] # takes the 'date' from the file name but it still has .csv on the end
            start_date = course_start.split('.')[0] # removes the .csv from the date
            column_names = list(df1.columns.values)  #gets the names of all the columns
            final_name =  column_names[-1]  #  gets the name of the last column for this particular table
            if len(final_name) <6: ## the length of the name varies depending on whether its an 8 or 10 week course
                course_length = final_name[-1] ##  this is for the 8 week courses
            else:
                course_length = final_name[-2] + final_name[-1]  ## this is for the 10 week courses
            df1['Course'] = conc  # creates an extra column in the dataframe called course that contains the concatenated course name
            df1['Start_Date'] = start_date  # creates an extra column that contains the date
            df1['Course_Length'] = course_length  # makes an extra column that will have the course length
            df_list.append(df1) ## adds data frame to a list of dataframes to all be returned at once when all files have been iterated through
        else:
            pass
    df = pd.concat(df_list)
    return df

def dateformat(bucket, folder,
               col):  # takes in the bucket and folder and creates df using above function & formats column specified to date
    df = dataframe(bucket, folder)
    df[col] = pd.to_datetime(df[col])  # format the date
    return df


def academy_formatter(bucket,folder):  # a function that converts all the numbers to numeric
    df = dateformat(bucket, folder, 'Start_Date')
    names = list(df.columns.values) # get the list of the names of all the columns
    strings = ['Start_Date','name', 'trainer', 'Course'] # the list of ones that we don't want to be turned into numeric
    for y in strings: # remove all the non-numeric ones from the list of column names
        names.remove(y)
    for x in names: # turns all the number ones into a numerical data type
        df[x] = pd.to_numeric(df[x])
    return df  # outputs a dataframe



###### ['IH', 'IS', 'PV', 'PS', 'SD', 'SA']  # this is a list of all the abbreviated behaviours
def splitter(bucket, comp):
    df = academy_formatter(bucket, 'Academy')
    names = list(df.columns.values)
    x = ['name']  # make a list of columns that we want to be included alongside the behaviour scores
    for y in names:  # for each of the column names in the list of column names
        if comp in y:  # if the abbreviated letters occur as a substring in the column name
            x.append(y)  # then add that column name onto the list of columns that we want to be included
    frame = df[x]  # make a new dataframe, made it from the original dataframe but only include the columns which we added to our list above
    return frame

def getCandIDs(): #makes a table with just the namecon and ID
    IDs = talentfile()
    df = IDs.drop([ 'name', 'gender', 'dob', 'email', 'city', 'address', 'postcode', 'phone_number', 'uni', 'degree', 'invited_date', 'month', 'invited_by'], axis=1)
    return df

def addIDs(comp):  # makes table for each comp with the correct IDs
    scores = splitter('data8-engineering-project', comp)
    scores = namecon(scores)
    IDs = getCandIDs()
    df = pd.merge(scores, IDs, on="namecon")
    df = df.drop(['namecon', 'name', 'id'], axis =1)
    names = list(df.columns.values)
    df = df.fillna(0.0)
    return df

######### ALEX ALL YOU NEED TO DO IS RUN THIS FOR EACH COMP ['IH', 'IS', 'PV', 'PS', 'SD', 'SA']

# print(addIDs('IH'))


