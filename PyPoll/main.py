import os
import csv

print("\nElection Results")
print("--------------------------------------------------")

# Relative path for input file
csvPath = os.path.join('..', 'Resources', 'election_data.csv')

# Relative path for output file 
output_path = os.path.join('..', 'analysis', 'py_poll_output.txt')

# Variable for total votes 
total_votes = 0 

# List to hold votes cast for each candidate 
candidates_list = []

# Dictonary to hold each candidate and the number of votes they received
candidates = {}

with open(csvPath) as csvFileStream:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvFileStream, delimiter =',')
    
    # Read the header row first
    csv_header = next(csv_reader)

    # For each row after the header... 
    for row in csv_reader: 
        
        # Add candidate's name to list each time a vote is cast in their name
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

# Calculating the percentage of votes for each candidate
khan_percentage = candidates["Khan"] / total_votes
khan_percentage = "{:.3%}".format(khan_percentage)

correy_percentage = candidates["Correy"] / total_votes
correy_percentage = "{:.3%}".format(correy_percentage)

li_percentage = candidates["Li"] / total_votes
li_percentage = "{:.3%}".format(li_percentage)

otooley_percentage = candidates["O'Tooley"] / total_votes
otooley_percentage = "{:.3%}".format(otooley_percentage)

# Getting candidate with the most votes from dictionary, 
# Setting that candidate as the winner
winner = max(candidates, key = candidates.get)

# Printing outputs
print(f"Total Votes: {total_votes}")
print("--------------------------------------------------")

print(f'Khan: {khan_percentage} ({candidates["Khan"]})')
print(f'Correy: {correy_percentage} ({candidates["Correy"]})')
print(f'Li: {li_percentage} ({candidates["Li"]})')
print("O'Tooley: " + str(otooley_percentage) + " (" + str(candidates['O\'Tooley']) + ")")
print("--------------------------------------------------")
print(f'Winner: {winner}')
print("--------------------------------------------------\n")


# Writing to the text file 
with open(output_path, 'w') as txt_file:

    txt_file.write("Election Results\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f'Khan: {khan_percentage} ({candidates["Khan"]})\n')
    txt_file.write(f'Correy: {correy_percentage} ({candidates["Correy"]})\n')
    txt_file.write(f'Li: {li_percentage} ({candidates["Li"]})\n')
    txt_file.write("O'Tooley: " + str(otooley_percentage) + " (" + str(candidates['O\'Tooley']) + ")\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f'Winner: {winner}\n')
    txt_file.write("---------------------------------------\n")
