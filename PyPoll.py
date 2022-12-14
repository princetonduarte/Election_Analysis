# The data we need to retieve.
# 1. The total number of votes cast
# 2. A complete list of candiates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote

import csv

import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options =[]
# Declare the empty dictionary. 3.5.3
candidate_votes = {}

# Winning Candidate and Winning Count Tracker. 3.5.5
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candiate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
             # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candiate's vote count. 3.5.3
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count. 3.5.3
        candidate_votes[candidate_name] += 1
        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    # Determine the percentage of votes for each candidate by looping through the counts. 3.5.4
    # Iterate throught he candidate list.
    for candidate_name in candidate_votes:
        # Retrive vote count of a candidate. 3.5.4
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes. 3.5.4
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print(f"{candidate_name}: recevied {vote_percentage:.1f}% of the vote.")
        print(candidate_results)
        # Save the candidate reults to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count. 3.5.5..added all the if statement
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # print out each candidate's name, vote count, and percentage of votes to the terminal. 
    # print statement needed to be on the if statement
        ##print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


