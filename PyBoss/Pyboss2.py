#working with
import os

import csv


# setting the path
#csvpath = os.path.join('raw_data', input_file)

#initial variables
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []
# cool feature that allows entry of file names for future files 
#!!!!!since this would take SOOO much of my TA's valuable time I have added duplicates of both data files included in the
#excersise these two options are a.csv and b.csv
input_file = input("What is the filename you need to analyze? "

csvpath = os.path.join("raw_data",input_file)
output_path = os.path.join("EmpinfoOutput"," newempinfo.csv")

# state dictionary from http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
#read in file with header
with open(csvpath,newline="")as input_file:
    csv_input = csv.reader(input_file, delimiter=',')
    header = next(input_file)
#create output file and write reordered/name headers
#create seperate lists for each value then zip together

    for row in csv_input:
         emp_id.append(row[0])

    #split Name on space character and write into two lists

         name_split = row[1].split(" ")     
         first_name_spl = name_split[0]   
         last_name_spl = name_split[1]
         first_name.append(first_name_spl)
         last_name.append(last_name_spl)
        
    #format birthdate

         bday_old_fmt = row[2].split("-")
         bday_new_fmt =  bday_old_fmt[1]+"/"+ bday_old_fmt[2]+"/"+ bday_old_fmt[0]
         dob.append(bday_new_fmt)

    #append matching state abbreviation

         state.append(us_state_abbrev[row[4]])
    # mask ssn
         ssn_split = row[3].split("-")
         ssn_masked = "***-**-"+str(ssn_split[2])
         ssn.append(ssn_masked)

#zip to define new list
    new_emp_data = zip(emp_id,first_name,last_name,dob,ssn,state)
#make the new lists and populate with that good data
emp_data_list = list(new_emp_data)
print(emp_data_list[0])


#add some headers in so we know what is what
with open(output_path, 'w',newline='') as pyboss_file_out:
    writer = csv.writer(pyboss_file_out, delimiter =',')
    new_headers=["Emp ID","First Name","Last Name","DOB","SSN","State"]
    writer.writerow(new_headers)
#fill up rows with all that good data
    with open(output_path, 'w',newline='') as pyboss_file_out:
        for row in emp_data_list:
            writer.writerow(row)




        




    