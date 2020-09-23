# PyBank Homework Script 

# Import os module 
import os 
# Import module for reading csv files 
import csv

# Printing header (may want to move this later)
print("Financial Analysis")
print("--------------------------------------------------")

# Commenting out relative path for now.. 
# NEED TO SWITCH TO THIS BEFORE SUBMITTING
# csvPath = os.path.join('..', 'Resources', 'budget_data.csv')

# Absolute path.. used JUST for testing purposes
csvPath = r"/Users/chloe/Documents/HW_ASSIGNMENTS/python-challenge/PyBank/Resources/budget_data.csv"

# Variable for total number of months 
months = 0

# Variable for net total amount of "profit/losses"
net_total = 0 

# Variable for change 
change = 0 

# Variable for avg change 
avg_change = 0 

# List to hold profits and losses 
profit_loss = []

# Variable for change 
change = 0 

# Variable for average change 
avg_change = 0 

with open(csvPath) as csvFileStream:
    # CSV reader specifies delimiter and variable that holds contents
    csvReader = csv.reader(csvFileStream, delimiter =',')
    
    # Read the header row first
    csv_header = next(csvReader)

    # For each row after the header...
    for row in csvReader:
        
        # Count the total number of months included in the dataset
        months += 1

        # Calculate net total of profits/losses over the entire period
        net_total += int(row[1])

        # Adding each profit/loss to the profit_loss list 
        profit_loss.append(int(row[1]))

# List comprehension to calculate successive difference in order to later calculate average change
change = [profit_loss[i+1] - profit_loss[i] for i in range (len(profit_loss)-1)]

# Calculating average change 
avg_change = sum(change) / len(change)

avg_change = "{:.2f}".format(avg_change)

#Printing outputs 
print(f"Total Months: {months}")
print(f"Total: ${net_total}")
print(f"Average  Change: (${avg_change})")
