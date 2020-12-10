import os
import csv

print ("Financial Analysis")
print ("----------------------------------------------")

# Set path for file
bank_data_csv = os.path.join("Resources", "budget_data.csv")


# Open the CSV
with open(bank_data_csv) as datafile:
    datafile_reader = csv.reader(datafile, delimiter=",")
 
    # Get rid of headers
    next(datafile_reader)

    # Find number of months in total 
    numline = len(list(datafile_reader))
    print ("Total Months:", (numline))

with open(bank_data_csv) as datafile:
    datafile_reader = csv.reader(datafile, delimiter=",")
    next(datafile_reader)
    # Calculate net total amount of "Profit/Losses"
    total = 0
    for row in datafile_reader:
       total += float(row[1])
    print ("Total: $"+str((total)))
    


