# PyPoll Homework

# Import Dependencies
import os
import csv


#Define the source data
election_csv=os.path.join("..","Resources","election_data.csv")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_list = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0


#Read the csv file
with open (election_csv, "r") as csvfile:
    #split the file at commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header line
    header = next(csvreader)
    
    for row in csvreader:
        #print (row)

        #Add to total vote count
        total_votes = total_votes + 1
        
        # Get candidate name from row
        candidate_name = row[2]
        
        # If the candidate is not on list
        if candidate_name not in candidate_list:

            # Add new candidate to candidate list
            candidate_list.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


#Define Output path
output_path = os.path.join("..", "Analysis", "ElectionAnalysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')    
    
    # Create Total Votes Summary
    votes_summary = (
     f'Election Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'-------------------------\n')

    # Print the Total Votes Summary (to terminal)
    print(votes_summary)  
        
    # Write the Total Votes Summary
    csvwriter.writerow([votes_summary])
    
    
    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Create Candidate Summary
        candidate_summary  = f'{candidate}: {vote_percentage:.3f}% ({votes})\n'

        # Print the output (to terminal)
        print(candidate_summary) 

        # Write the Total Votes Summary
        csvwriter.writerow([candidate_summary])


    # Create Winner Summary
    winner_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'-------------------------\n')

    # Print the output (to terminal)
    print(winner_summary)  

    # Write the Total Votes Summary
    csvwriter.writerow([winner_summary]) 
