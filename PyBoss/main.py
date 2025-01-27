import os
import csv 
import datetime

from us import us_state_abbrev

# Relative path for input file
csvPath = os.path.join('Resources', 'employee_data.csv')

# Relative path for output file
output_path = os.path.join('analysis', 'py_poll_output.txt')

# List to hold all first names from the dataset after splitting
first_name = []

# List to hold all last names from the dataset after splitting
last_name = []

# List to hold all the reformatted dates 
date_formatted = []

# List to hold all of the hidden SSN numbers 
hidden_ssn = []

# List to hold the abbreviated state name 
state = []

with open(csvPath) as csvFileStream:

    csv_reader = csv.reader(csvFileStream, delimiter = ',')

    csv_header = next(csv_reader)

    for row in csv_reader:
        # Splitting first and last name
        first = row[1].split()[0]
        last = row[1].split()[1]

        first_name.append(first)
        last_name.append(last)

        # Reformatting date
        date = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y')
        date_formatted.append(date)

        # Hiding SSN 
        ssn = row[3].split("-")
        hidden_ssn.append("***-**-" + ssn[2])

        # Using provided dictionary to abbreviate the state name 
        state.append(us_state_abbrev[row[4]])

with open(output_path, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Writing the headers to the csv file 
    csv_writer.writerow(["First Name", "Last Name", "DOB", "SSN", "State"])
    # Writing the new data to the csv file 
    csv_writer.writerows(zip(first_name, last_name, date_formatted, hidden_ssn, state))

    csv_file.close()
