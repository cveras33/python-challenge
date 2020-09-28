import os 
import csv

print("\nFinancial Analysis")
print("--------------------------------------------------")

# Relative path for input file
csvPath = os.path.join('Resources', 'budget_data.csv')

# Relative path for output file 
output_path = os.path.join('analysis', 'py_bank_output.txt')

# List for all the dates in the dataset
months = []

# Varible for the number of months in the dataset 
num_months = 0 

# Variable for net total amount of profit/losses
net_total = 0 

# List to hold profits and losses 
profit_loss = []

# Variable for change 
change = 0 

# Variable for average change 
avg_change = 0 

# Variable for greatest profit increase amount 
greatest_increase = 0 

# Variable for greatest profit decrease amount 
greatest_decrease = 0

with open(csvPath) as csvFileStream:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvFileStream, delimiter =',')
    
    # Read the header row first
    csv_header = next(csv_reader)

    # For each row after the header...
    for row in csv_reader:
        
        # Add each date to the months list
        months.append(row[0])

        # Calculate net total of profits/losses over the entire period
        net_total += int(row[1])

        # Add each profit/loss to the profit_loss list 
        profit_loss.append(int(row[1]))

# Getting the total number of months in the dataset 
num_months = len(months)

# List comprehension to calculate successive difference in order to later calculate average change
change = [profit_loss[i+1] - profit_loss[i] for i in range (len(profit_loss)-1)]

# Calculating average change 
avg_change = sum(change) / len(change)

# Formatting average change to print to two decimal places
avg_change = "{:.2f}".format(avg_change)

# Getting greatest increase in profits amount from change list 
greatest_increase = max(change)

# Getting the month with the greatest increase in profits
greatest_increase_month = change.index(max(change)) + 1

# Getting greatest decrease in profits amount from change list 
greatest_decrease = min(change)

# Getting the month with the greatest decrease in profits
greatest_decrease_month = change.index(min(change)) + 1

# Printing outputs 
print(f"Total Months: {num_months}")
print(f"Total: ${net_total}")
print(f"Average  Change: (${avg_change})")
print(f"Greatest Increase in Profits: {months[greatest_increase_month]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {months[greatest_decrease_month]} (${greatest_decrease})\n")

# Writing to the text file 
with open(output_path, 'w') as txt_file:

    txt_file.write("Financial Analysis\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"Total Months: {num_months}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average  Change: (${avg_change})\n")
    txt_file.write(f"Greatest Increase in Profits: {months[greatest_increase_month]} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {months[greatest_decrease_month]} (${greatest_decrease})")

    #Is this where you would close? 