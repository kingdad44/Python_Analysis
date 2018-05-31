#working with
import os

import csv

# setting the path
csvpath = os.path.join('raw_data', 'employee_data1.csv')

#initial variables
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

input_file = input("What is the filename you need to analyze?  ")
csvpath = os.path.join("raw_data",input_file)

# state dictionary from http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
us_state_abbrev = states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

#read in file with header
with open(csvpath,newline="")as input_file:
    csvreader = csv.reader(input_file, delimiter=',')
    reader = csv.DictReader(input_file)
    header = next(input_file)

   # looping through the read file
    for row in csvreader:
        # appending employee id to a new list
        emp_id.append(row[0])

        # appending first & last name to two separate lists
        name = row[1].split(" ") # splitting name by space
        first_name.append(name[0]) # appending first name
        last_name.append(name[1]) # appending last name

        # formatting & appending dob
        bdate = row[2].split("-") # splitting dob by '-'
        new_db = bdate[1] + "/" + bdate[2] + "/" + bdate[0] # formatting dob
        dob.append(new_db) # appending formatted dob

        #formatting & appending ssn
        ssn_split = row[3].split("-") # splitting ssn by '-'
        new_ssn = "***-**-" +ssn_split[2] # formatting ssn
        ssn.append(new_ssn) # appending formatted ssn

        # looping through states dictionary
        state.append(us_state_abbrev[row[1]])

# tests
    print(first_name[0])
    print(last_name[0])
    print(dob[0])
    print(ssn[0])
    print(state[0])

# zipping data
employees = zip(emp_id, first_name, last_name, dob, ssn, state)

# creting the new csv file
output_file = os.path.join('Output/employee_data_clean_2.csv')

# opening & writing the file
with open(output_file, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')

    # writing in headers
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # writing data
    for employee in employees:
        writer.writerow(employee)        



