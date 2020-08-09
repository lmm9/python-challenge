# Import Dependencies
import os
import csv
import datetime

#Define the source data
budget_csv=os.path.join("..","Resources","budget_data.csv")

#Read the csv file
with open (budget_csv, "r") as csvfile:
    #split the file at commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header line
    header = next(csvreader)
    #test to ensure data present
    print (header)
    
    #Convert date column to time format and profit to integer
    date=datetime.datetime(budget_data[0], "%b-%Y")
    profit=int(budget_data[1])
         
    # Calculate First and Last Values
    open_date==0
    close_date==0
    for i in range(0,len(profit)): 
        if open_date>date[i]:
            open_date=date[i]
            open_profit=profit[i]
            if close_datet<date[i]:
                close_date=date[i]
                close_profit=profit[i]

    
    # Calculate Max and Min profit and dates
    max_profit ==0   
    min_profit==0    
    for i in range(0,len(profit),1): 
        if max_profit<profit[i]:
            max_profit=profit[i]
            max_date=date[i]
            if min_profit>profit[i]:
                min_profit=profit[i]
                min_date=date[i]

     total_months=close_date-open_date
     total_profit=close_profit-open_profit

#Define Output path
output_path = os.path.join("..", "Analysis", "FinancialAnalysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the Summary Headers
    csvwriter.writerow(["'''text")
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-----------------"])
    

    # Write the Summary Info
    csvwriter.writerow(["Total Months: "+total_months])
    csvwriter.writerow(["Total: "+total_profit])
    csvwriter.writerow(["Average Change: "+avg_profit])
    csvwriter.writerow(["Greatest Increase in Profits: "+str(max_date)+ " ("+str(max_profit)+")"])
    csvwriter.writerow(["Greatest Decrease in Profits: "+str(min_date)+ " ("+str(min_profit)+")"])
    


