#PyBank Homework

# Import Dependencies
import os
import csv

#Define the source data
budget_csv=os.path.join("..","Resources","budget_data.csv")


# Track various financial parameters
total_months = 0
month_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]
total_net = 0

#Read the csv file
with open (budget_csv, 'r') as csvreader:
    #split the file at commas
    csvreader = csv.reader(csvreader, delimiter=',')
    #Skip the header line
    header = next(csvreader)
    
    #Read the first row to calculate net change
    first_row = next(csvreader)
    total_months +=1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    for row in csvreader:

        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list += [net_change]
        month_change += [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_month_avg = sum(net_change_list) / len(net_change_list)

# Create Financial Analysis Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_month_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)


#Define Output path
output_path = os.path.join("..", "Analysis", "FinancialAnalysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as output_file:

    # Initialize csv.writer
    csvwriter = csv.writer(output_file, delimiter=',')
    
    # Write the output
    csvwriter.writerow([output])
    
  