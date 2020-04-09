import boto3
import pandas as pd
from AcademiesTable import *
import pyodbc
from strength_weakness_tech import *
from Trainers import *
from Talent_Team import *
from courses_table import *
from interview_assessment import *
from BehavioursTablesFINAL import *
from CandidateTable import *
from Candidate_strengths_weaknesses import *
from Candidate_tech import *


server = 'localhost,1433'
database = 'sparta'
username = 'SA'
password = 'Passw0rd2018'
docker_sparta = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = docker_sparta.cursor()

cursor.execute("SELECT @@version;")

def strengths_table_import():
    strengths()
    for index, row in strengths().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Strengths (strength_ID, strength_name) VALUES (?,?)", row['StrengthID'], row['StrengthName'])


    docker_sparta.commit()

def weaknesses_table_import():
    for index, row in weaknesses().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Weaknesses (weakness_ID, weakness_name) VALUES (?,?)", row['WeaknessID'], row['WeaknessName'])

    docker_sparta.commit()

def technologies_table_import():
    for index, row in tech().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Technologies (technology_ID, technology_name) VALUES (?,?)", row['TechID'], row['TechName'])

    docker_sparta.commit()

def academies_table_import():
    for index, row in academiestable().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Academies (academy_ID, academy_name) VALUES (?,?)", row['AcademyID'], row['academy'])

    docker_sparta.commit()

def trainers_table_import():
    for index, row in trainerstable().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Trainers (trainer_ID, first_name, last_name) VALUES (?,?,?)", row['TrainerID'], row['first_name'], row['last_name'])

    docker_sparta.commit()

def talent_table_import():
    for index, row in talentteamtable().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Talent_Team (talent_person_ID, first_name, last_name) VALUES (?,?,?)", row['Talent_Team_ID'], row['first_name'], row['last_name'])

    docker_sparta.commit()

def course_types_table_import():
    for index, row in course_types().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Course_Types (course_type_ID, course_name) VALUES (?,?)", row['course_type_ID'], row['Course Type'])

    docker_sparta.commit()

def courses_table_import():
    for index, row in courses_table().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Courses (course_ID, course_type_ID, course_number, course_length_weeks, start_date, trainer_ID) VALUES (?,?,?,?,?,?)", row['CourseID'], row['course_type_ID'], row['Course Number'], row['Course_Length'], row['Start_Date'], row['TrainerID'])

    docker_sparta.commit()

def interview_assesment_table_import():
    for index, row in interviewnotes().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Interview_Assesment (candidate_ID, psychometrics_score, presentation_score, geo_flex, self_development, financial_support, result, course_type_ID, academy_ID, interview_date) VALUES (?,?,?,?,?,?,?,?,?,?)", row['CandidateID'], row['psychometrics'], row['presentation'], row['geo_flex'], row['self_development'], row['financial_support_self'], row['result'], row['course_type_ID'], row['AcademyID'], row['date'])

        docker_sparta.commit()

def IH_table_import():
    for index, row in addIDs('IH').iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Horsepower (candidate_id, week_1, week_2, week_3, week_4, week_5, week_6, week_7, week_8, week_9, week_10) VALUES (?,?,?,?,?,?,?,?,?,?,?)", row['CandidateID'], row['IH_W1'], row['IH_W2'], row['IH_W3'], row['IH_W4'], row['IH_W5'], row['IH_W6'], row['IH_W7'], row['IH_W8'], row['IH_W9'], row['IH_W10'])

    docker_sparta.commit()

def IS_table_import():
    for index, row in addIDs('IS').iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Interpersonal_Savvy (candidate_id, week_1, week_2, week_3, week_4, week_5, week_6, week_7, week_8, week_9, week_10) VALUES (?,?,?,?,?,?,?,?,?,?,?)", row['CandidateID'], row['IS_W1'], row['IS_W2'], row['IS_W3'], row['IS_W4'], row['IS_W5'], row['IS_W6'], row['IS_W7'], row['IS_W8'], row['IS_W9'], row['IS_W10'])

    docker_sparta.commit()

def PV_table_import():
    for index, row in addIDs('PV').iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Perseverance (candidate_id, week_1, week_2, week_3, week_4, week_5, week_6, week_7, week_8, week_9, week_10) VALUES (?,?,?,?,?,?,?,?,?,?,?)", row['CandidateID'], row['PV_W1'], row['PV_W2'], row['PV_W3'], row['PV_W4'], row['PV_W5'], row['PV_W6'], row['PV_W7'], row['PV_W8'], row['PV_W9'], row['PV_W10'])

    docker_sparta.commit()

def PS_table_import():
    for index, row in addIDs('PS').iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Problem_Solving (candidate_id, week_1, week_2, week_3, week_4, week_5, week_6, week_7, week_8, week_9, week_10) VALUES (?,?,?,?,?,?,?,?,?,?,?)", row['CandidateID'], row['PS_W1'], row['PS_W2'], row['PS_W3'], row['PS_W4'], row['PS_W5'], row['PS_W6'], row['PS_W7'], row['PS_W8'], row['PS_W9'], row['PS_W10'])

    docker_sparta.commit()

def SD_table_import():
    for index, row in addIDs('SD').iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Self_Development (candidate_id, week_1, week_2, week_3, week_4, week_5, week_6, week_7, week_8, week_9, week_10) VALUES (?,?,?,?,?,?,?,?,?,?,?)", row['CandidateID'], row['SD_W1'], row['SD_W2'], row['SD_W3'], row['SD_W4'], row['SD_W5'], row['SD_W6'], row['SD_W7'], row['SD_W8'], row['SD_W9'], row['SD_W10'])

    docker_sparta.commit()

def SA_table_import():
    for index, row in addIDs('SA').iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Standing_Alone (candidate_id, week_1, week_2, week_3, week_4, week_5, week_6, week_7, week_8, week_9, week_10) VALUES (?,?,?,?,?,?,?,?,?,?,?)", row['CandidateID'], row['SA_W1'], row['SA_W2'], row['SA_W3'], row['SA_W4'], row['SA_W5'], row['SA_W6'], row['SA_W7'], row['SA_W8'], row['SA_W9'], row['SA_W10'])

    docker_sparta.commit()

def candidates_table_import():
    for index, row in candidates_table().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Candidates (candidate_ID, first_name, last_name, gender, email, city, candidate_address, postcode, phone, university, degree, course_ID, talent_person_ID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", row['CandidateID'], row['first_name'], row['last_name'], row['gender'], row['email'], row['city'], row['address'], row['postcode'], row['phone_number'], row['uni'], row['degree'], row['CourseID'], row['Talent_Team_ID'])
        docker_sparta.commit()

def candidate_strengths_table_import():
    for index, row in candidate_strengths().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Candidate_Strengths (candidate_ID, strength_ID) VALUES (?,?)", int(row['CandidateID']), int(row['StrengthID']))
        docker_sparta.commit()

def candidate_weaknesses_table_import():
    for index, row in candidate_weaknesses().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Candidate_Weaknesses (candidate_ID, weakness_ID) VALUES (?,?)", int(row['CandidateID']), int(row['WeaknessID']))
        docker_sparta.commit()

def candidate_tech_table_import():
    for index, row in candidate_tech().iterrows():
        # print(index,row) #Test option
        cursor.execute("INSERT INTO SpartaDB.dbo.Candidate_Technologies (candidate_ID, technology_ID, self_score) VALUES (?,?,?)", (row['CandidateID']), int(row['self_score']), row['TechName'])
        docker_sparta.commit()

def import_all_but_tech():
    strengths_table_import()
    weaknesses_table_import()
    academies_table_import()
    trainers_table_import()
    talent_table_import()
    course_types_table_import()
    courses_table_import()
    interview_assesment_table_import()
    IH_table_import()
    IS_table_import()
    PV_table_import()
    PS_table_import()
    SD_table_import()
    SA_table_import()
    candidates_table_import()
    candidate_strengths_table_import()
    candidate_weaknesses_table_import()

import_all_but_tech()

# these are run separately because they take a long time to run
technologies_table_import()
candidate_tech_table_import()
