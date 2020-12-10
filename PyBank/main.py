import os
import csv

print ("Financial Analysis")
print ("----------------------------------------------")

# Set path for file
bank_data_csv = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(bank_data_csv) as datafile:
    datafilereader = csv.reader(datafile, delimiter=",")

    # Get rid of headers
    next(datafile)

    # Find number of months in total 
    numline = len(datafile.readlines())
    print ("Total Months:", (numline))




