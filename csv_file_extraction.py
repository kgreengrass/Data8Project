##not nicely packaged as a fucntion yet sorry
import boto3
from pprint import pprint
import csv

s3_client = boto3.client('s3')
contents = s3_client.list_objects_v2(Bucket='data8-engineering-project')['Contents']
a= 0
for x in contents:
    a = a + 1
    b= a
    splitfile = x['Key'].split('/')
    if splitfile[0] == 'Academy':   ###doesnt work because all the taqlent ones are more than 1000th in the list
        data = s3_client.get_object(Bucket='data8-engineering-project',
                                    Key = x['Key'])

        old_data = data['Body'].read().decode('utf-8').strip()
        old_data1 =(old_data.replace(' ', ''))
        old_data2 = old_data1.split()
        print(old_data2)

        csv_reader = csv.DictReader(old_data2)

        with open('Blank_CSV' + str(b) + '.csv', 'w') as new_file:
            fieldnames = ['name', 'trainer', 'IH_W1', 'IS_W1', 'PV_W1', 'PS_W1', 'SD_W1', 'SA_W1', 'IH_W2', 'IS_W2', 'PV_W2', 'PS_W2', 'SD_W2', 'SA_W2', 'IH_W3', 'IS_W3', 'PV_W3', 'PS_W3', 'SD_W3', 'SA_W3', 'IH_W4', 'IS_W4', 'PV_W4', 'PS_W4', 'SD_W4', 'SA_W4', 'IH_W5', 'IS_W5', 'PV_W5', 'PS_W5', 'SD_W5', 'SA_W5', 'IH_W6', 'IS_W6', 'PV_W6', 'PS_W6', 'SD_W6', 'SA_W6', 'IH_W7', 'IS_W7', 'PV_W7', 'PS_W7', 'SD_W7', 'SA_W7', 'IH_W8', 'IS_W8', 'PV_W8', 'PS_W8', 'SD_W8', 'SA_W8', 'IH_W9', 'IS_W9', 'PV_W9', 'PS_W9', 'SD_W9', 'SA_W9', 'IH_W10', 'IS_W10', 'PV_W10', 'PS_W10', 'SD_W10', 'SA_W10']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

            csv_writer.writeheader()

            for line in csv_reader:  # Iterates through the user_details file in read mode.
                csv_writer.writerow(line)





