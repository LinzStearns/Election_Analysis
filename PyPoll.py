# 1. Open the data file. The total number of votes cast. Count total votes.
# 2. First and Last name of each candidate that gets at least one vote.
# 3. Count how many votes each candidate got. 
# 4. Divide each candidates value for #3 by #1for percentage of votes per candidate.
# 5. Print the name of the winner based on popular vote
import os 
import csv
# Assign a variable for the file to load and the path. 
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
