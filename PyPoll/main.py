import os
import csv

# Printing header 
print("Election Results")
print("--------------------------------------------------")

# Relative path for input file
# csvPath = os.path.join('..', 'Resources', 'election_data.csv')

csvPath = r'/Users/chloe/Documents/HW_ASSIGNMENTS/python-challenge/PyPoll/Resources/election_data.csv'

# Variable for total votes cast 
total_votes = 0 

# List to hold vote cast for each candidate 
candidates_list = []

# Dictonary to hold each candidate and the number of votes they received
candidates = {}

with open(csvPath) as csvFileStream:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvFileStream, delimiter =',')
    
    # Read the header row first
    csv_header = next(csv_reader)

    for row in csv_reader: 
        candidates_list.append(row[2])

# Getting the total amount of votes cast        
total_votes = len(candidates_list)

# Adding each candidate to a dictionary and if they've already
# been added, adding one to their total number of votes
for candidate in candidates_list:
    if(candidate in candidates):
        candidates[candidate] += 1
    else:
        candidates[candidate] = 1

# Printing outputs
print(f"Total Votes: {total_votes}")
print("--------------------------------------------------")

print(candidates.keys())

#printing 
#for key, value in candidates.items():
#    print("%s : %d"%(key, value))
