import boto3
import pandas as pd


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
            course_type = name.split('_')[0]##splits the file up and takes the first part of it i.e. 'business', 'data'
            course_initial = course_type[0]
            course_number = name.split('_')[1]  ####takes the second entry, i.e. a number
            conc = course_initial + course_number ####concatenates the course type and the number of which group it is
            course_start = name.split('_')[2] # takes the 'date' from the file name but it still has .csv on the end
            start_date = course_start.split('.')[0] # removes the .csv from the date
            column_names = list(df1.columns.values)  #gets the names of all the columns
            final_name =  column_names[-1]  #  gets the name of the last column for this particular table
            if len(final_name) <6: ## the length of the name varies depending on whether its an 8 or 10 week course
                course_length = final_name[-1] ##  this is for the 8 week courses
            else:
                course_length = final_name[-2] + final_name[-1]  ## this is for the 10 week courses
            df1['CourseID'] = conc  # creates an extra column in the dataframe called course that contains the concatenated course name
            df1['Course Type'] = course_type
            df1['Course Number'] = course_number
            df1['Start_Date'] = start_date  # creates an extra column that contains the date
            df1['Course_Length'] = course_length  # makes an extra column that will have the course length
            df2 = df1[['CourseID', 'Course Type', 'Start_Date', 'Course_Length', 'trainer','Course Number' ]].iloc[:1]
            df_list.append(df2) ## adds data frame to a list of dataframes to all be returned at once when all files have been iterated through
        else:
            pass
    df = pd.concat(df_list)
    return df

def dateformat(col):  # takes in the bucket and folder and creates df using above function & formats column specified to date
    df = dataframe('data8-engineering-project', 'Academy')
    df[col] = pd.to_datetime(df[col])
    return df
