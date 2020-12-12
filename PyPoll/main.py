import os
import csv

print ("Election Results")
print ("----------------------------------------------")

# Set path for file
poll_data_csv = os.path.join("Resources", "election_data.csv")

# Open the CSV, find number of votes
with open(poll_data_csv) as datafile:
    datafile_reader = csv.reader(datafile, delimiter=",")

    # Get rid of headers
    next(datafile_reader)

    # Total number of votes cast
    total_votes = len(list(datafile_reader))
    print ("Total Votes:", (total_votes))

print ("----------------------------------------------")

# Open the CSV, find number of candidates

# Create list for full candidate name 
candidate_name = []


with open(poll_data_csv) as datafile:
    datafile_reader = csv.reader(datafile, delimiter=",")

    # Skip Header
    fields = next(datafile_reader)

    # Populate candidate_name list 
    for row in datafile_reader:
        candidate_name.append(row[2])
    
    # Use 'set' to pull unique candidate names
    unique_candidate = set(candidate_name)
    unique_candidate = list(unique_candidate)


    # find and print percentage of votes and number of votes from each candidate
    Khan_votes = candidate_name.count("Khan")
    Khan_percentage = "{:.0%}".format(Khan_votes/total_votes)
    print (f'Khan: {Khan_percentage} ({Khan_votes})')
    
    Correy_votes = candidate_name.count("Correy")
    Correy_percentage = "{:.0%}".format(Correy_votes/total_votes)
    print (f'Correy: {Correy_percentage} ({Correy_votes})')
    
    Li_votes = candidate_name.count("Li")
    Li_percentage = "{:.0%}".format(Li_votes/total_votes)
    print (f'Li: {Li_percentage} ({Li_votes})')
    
    OTooley_votes = candidate_name.count("O'Tooley")
    OTooley_percentage = "{:.0%}".format(OTooley_votes/total_votes)
    print (str("O'Tooley:"), f'{OTooley_percentage} ({OTooley_votes})')
    
    print ("----------------------------------------------")

    print ("Winner: Khan")

# write everything to text file
#define output path
output_file = os.path.join("analysis.txt")


#write to text file
with open(output_file, "w", newline='') as datafile:
    datafile.write("Election Results\n")
    datafile.write("----------------------------------------------\n")
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write("----------------------------------------------\n")
    datafile.write(f'Khan: {Khan_percentage} ({Khan_votes})\n')
    datafile.write(f'Correy: {Correy_percentage} ({Correy_votes})\n')
    datafile.write(f'Li: {Li_percentage} ({Li_votes})\n')
    datafile.write(str("O'Tooley:")+ f'{OTooley_percentage} ({OTooley_votes})\n')
    datafile.write("----------------------------------------------\n")
    datafile.write("Winner: Khan")