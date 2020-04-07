import pandas as pd

def inputspace(row):  # function for asking for user input for where the space should be
    while True:  # checks input is a number and in range of number of spaces
        try:
            space = int(input(f'{row} \n '  # asks for input on where to split the name
                          f'Please input number for the space that separates first and last name i.e. '
                          f'input 1 for 1st space, 2 for 2nd space etc.: '))
            if 1 <= space <= row.count(' '):
                splits = row.split(' ')  # splits by all spaces
                # creates the name as a list, joining the relevant number splits to give the correct first and second name:
                name = [' '.join(splits[:space]), ' '.join(splits[space:])]
                return name
        except (ValueError, TypeError):  # won't pass the try if the string can't be changed into an integer
            pass

def splitname(name):  # takes in the name column of a dataframe
    name_list=[]
    for row in name:  # goes through each row of the file being uploaded
        row=row.strip()  # strips any whitespace off beginning and end
        if row.count(' ') == 1:  # checks to see if only the one space
            name_list.append(row.split(" ", 1))  # automatically splits name into first and last and adds to list
        else:
            name_list.append(inputspace(row))  # adds the name from the manually choosing space to split function
    namedf = pd.DataFrame(name_list)  # creates a dataframe from the name list created above
    return namedf  # returns a dataframe of first and last name


interview_df = pd.read_csv('C:/Users/TECH-W80.LT-RICH-W80/Desktop/cleaning dev/interview_notes1.csv')
df = pd.DataFrame([['Casian Pavel'], ['Anna Maia Caruso']],
                  columns=['name'])
print(splitname(interview_df.name))
