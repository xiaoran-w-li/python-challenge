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

# Calculate net total amount of "Profit/Losses"
with open(bank_data_csv) as datafile:
    datafile_reader = csv.reader(datafile, delimiter=",")
    next(datafile_reader)

    total = 0
    for row in datafile_reader:
       total += float(row[1])
    print ("Total: $"+str((total)))


#Calculate average profit/losses and max proft and max loss
with open(bank_data_csv) as datafile:
    datafile_reader = csv.reader(datafile, delimiter=",")
    next(datafile_reader)

    #list to store revenue data
    revenue = []
    #list of average change in revenue 
    change_revenue = []
    #list of dates
    date = []


    #populate list with second column [1] profit losses
    #populate list with first column [0] date
    for row in datafile_reader:
        revenue.append(float(row[1]))
        date.append(row[0])
    
    #loop to find revenue change in newly populated revenue list
    for i in range(1,len(revenue)):
        change_revenue.append(revenue[i] - revenue[i-1])
        average_change_revenue = sum(change_revenue)/len(change_revenue)

        max_change_revenue = max(change_revenue)

        min_change_revenue = min(change_revenue)

        date_max_change_revenue = str(date[change_revenue.index(max(change_revenue))+1])
        date_min_change_revenue = str(date[change_revenue.index(min(change_revenue))+1])

    print ("Average Change: $"+str(average_change_revenue))
    print ("Greatest Increase in Profits:", (date_max_change_revenue), "$"+str(max_change_revenue))
    print ("Greatest Decrease in Profits:", (date_min_change_revenue), "$"+str(min_change_revenue))



