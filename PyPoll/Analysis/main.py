# Import Dependenciesimport osimport csv#Define the source dataelection_csv=os.path.join("..","Resources","election_data.csv")#Read the csv filewith open (election_csv, "r") as csvfile:    #split the file at commas    csvreader = csv.reader(csvfile, delimiter=',')    #Skip the header line    header = next(csvreader)    #test to ensure data present    print (header)        #Convert Voter ID to integer    voter_id=int(election_data[0])             # Calculate Votes    total_votes =0     cand_1= "Correy"    cand_2= "Khan"    cand_3="Li"    cand_4="O'Tooley"    cand1_votes=0    cand2_votes=0    cand3_votes=0    cand4_votes=0    for i in range(0,len(voter_id)):         total_votes=total_votes+1        if cand1==candidate[i]:            cand1_votes=cand1_votes +1          elif cand2==candidate[i]:            cand2_votes=cand2_votes +1        elif cand3==candidate[i]:            cand2_votes=cand3_votes +1        elif cand3==candidate[i]:            cand3_votes=cand3_votes +1        elif cand4==candidate[i]:            cand4_votes=cand4_votes +1                       #Calculate Percentages      cand1_percent=cand1_votes/total_votes      cand2_percent=cand1_votes/total_votes      cand3_percent=cand1_votes/total_votes      cand4_percent=cand1_votes/total_votes        if cand1_percent>cand2_percent and cand1_percent>cand3_percent and cand1_percent>cand4_percent        winner=cand_1    elif cand2_percent>cand1_percent and cand2_percent>cand3_percent and cand2_percent>cand4_percent        winner=cand_2    elif cand3_percent>cand1_percent and cand3_percent>cand2_percent and cand3_percent>cand4_percent        winner=cand_3    elif cand4_percent>cand1_percent and cand4_percent>cand2_percent and cand4_percent>cand3_percent        winner=cand_4 #Define Output pathoutput_path = os.path.join("..", "Analysis", "ElectionAnalysis.csv")# Open the file using "write" mode. Specify the variable to hold the contentswith open(output_path, 'w') as csvfile:    # Initialize csv.writer    csvwriter = csv.writer(csvfile, delimiter=',')    # Write the Summary Headers    csvwriter.writerow(["'''text"])    csvwriter.writerow(["Election Results"])    csvwriter.writerow(["-----------------"])        # Write the Total Votes    csvwriter.writerow(["Total Votes: "+total_votes])    csvwriter.writerow(["-----------------"])        # Write the Candidate Percentages    csvwriter.writerow([+cand_1+ ":  " +cand1_percent+ " "+cand1_votes])    csvwriter.writerow([+cand_2+ ":  " +cand2_percent+ " "+cand2_votes])    csvwriter.writerow([+cand_3+ ":  " +cand3_percent+ " "+cand3_votes])    csvwriter.writerow([+cand_4+ ":  " +cand4_percent+ " "+cand4_votes])        #Write Winner    csvwriter.writerow(["-----------------"])    csvwriter.writerow(["WINNER:  "+winner])    csvwriter.writerow(["-----------------"])