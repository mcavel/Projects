# Import Modules
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    revenue = float(0)
    differencesum=float(0)
    revenuelist = []
    revenuechanges = []
    monthlist = []
    change=float(0)
    r=int(0)
    maxmimum=float(0)

    #Loop through rows; sum and store revenue; store month
    for row in csvreader:
        revenue = float(revenue)+float(row[1])
        revenuelist.append(row[1])
        monthlist.append(row[0])
        
    #zip revenue list against itself(with the second half pushed out by one); 
    for x, y in zip(revenuelist, revenuelist[1:]):
        #find and store difference
        difference = float(y)-float(x)
        revenuechanges.append(difference)

    #find max and min amounts and assign variables   
    maxamount = max(revenuechanges)
    minamount = min(revenuechanges)  
    
    #zip monthlist and changes together
    revenue_data= zip(monthlist, revenuechanges) 
    #loop through; find max and min, and return the months
    for i in revenue_data:
        if i[1]== maxamount:
            maxamountlabel=i[0]
        elif i[1] == minamount:
            minamountlabel= i[0]
           
print('\n'
"Financial Analysis" + '\n' 
"----------------------------"+'\n'
"Total Months:  " + str(int(len(revenuelist))) + '\n'
"Revenue:  $" + str(int(revenue)) + '\n' 
"Average Revenue Change: $"  + str(int((revenue)/(len(revenuelist)))) + '\n'
"Greatest Increase in Revenue:  " + str(maxamountlabel) + " (" + str(int(maxamount)) +")" '\n'
"Greatest Decrease in Revenue:  " + str(minamountlabel) + " (" + str(int(minamount)) +")" '\n')

# Specify the file to write to
output_path = os.path.join('output', 'pybank.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------------------------'])
    # Write the second row
    csvwriter.writerow(['Total Months:  ', str(int(len(revenuelist)))])
    csvwriter.writerow(['Revenue: ', str(int(revenue))])
    csvwriter.writerow(['Average Revenue Change:  ', str(int((revenue)/(len(revenuelist))))])
    csvwriter.writerow(['Greatest Increase in Revenue:  ', str(maxamountlabel),str(int(maxamount))])
    csvwriter.writerow(['Greatest Decrease in Revenue:  ',str(minamountlabel), str(int(minamount))])