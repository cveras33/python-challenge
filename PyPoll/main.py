import os
import csv

# Printing header 
print("Election Results")
print("--------------------------------------------------")

# Relative path for input file
# csvPath = os.path.join('..', 'Resources', 'election_data.csv')

csvPath = r"/Users/chloe/Documents/HW_ASSIGNMENTS/python-challenge/PyPoll/Resources/election_data.csv"

# Variable for total votes 
total_votes = 0 

# List to hold vote cast for each candidate 
candidates = []

with open(csvPath) as csvFileStream:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvFileStream, delimiter =',')
    
    # Read the header row first
    csv_header = next(csv_reader)

    # Calculating the total number of votes
    total_votes = sum(1 for row in csv_reader)

# Printing outputs
print(f"Total Votes: {total_votes}")
print("--------------------------------------------------")
