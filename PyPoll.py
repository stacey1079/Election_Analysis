import os 
import csv

# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election.analysis.txt')

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

#Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read and print the header row. 
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:

    # Add to the total vote count.
        total_votes += 1

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")

# Determine winning vote count and candidate
#1. Determine if the votes are greater than the winning count.
if (votes> winning_count) and (vote_percentage > winning_percentage):
    # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
    winning_count = votes
    winning_percentage = vote_percentage
    # 3. Set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name

# Print out each candidate's name, vote count, and percentage of votes to terminal.
print(f"{candidate_name}: {vote_percentage:.1f} ({votes:, })\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


