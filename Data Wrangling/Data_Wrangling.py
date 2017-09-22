
#US State Abbreviation Dictionary
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


# Import Modules
import os
import csv

# Set path for file
csvpath = os.path.join("employee_data1.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
#Set Lists
    ID=[]
    Name=[]
    DOB=[]
    SSN=[]
    STATE=[]
    FNAME=[]
    LNAME=[]
    SSN_P=[]
    STATE_AB=[]
#Loop through each row
    for row in csvreader:
        ID.append(row[0])
        #split first and last name by a space delimiter
        FFName = row[1].split(" ")
        FNAME.append(FFName[0])
        LLName = row[1].split(" ")
        LNAME.append(LLName[-1])
        #split and change date format from YYYY-MM-DD to DD/MM/YYYY
        tempdate = row[2].split("-")
        DOB.append(tempdate[0] + "/" + tempdate[1] + "/" + tempdate[2])
        ##hide first 5 SSN Digits by spliting using a demiliter of "-" and replacing it with hashtags
        SSNN = row[3].split("-")
        SSN_P.append("###-##-" + SSNN[2])
        #loop through dictionary; find abbreviation, store in list
        tempstate=row[4]
        for fstate, abst in us_state_abbrev.items():
            if(tempstate==fstate):
                STATE_AB.append(abst)
        #zip up all lists to be exported to csv format
        employee_info= zip(ID, FNAME,LNAME, DOB, SSN_P, STATE_AB) 
           

# Set variable for output file
output_file = os.path.join('output', 'pyboss.csv')

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

     # Write the header row
    writer.writerow(["ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(employee_info)
#