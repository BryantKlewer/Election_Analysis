# Add our dependencies
import csv
from email import header
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Print the header row
    headers = next(file_reader)
    print(headers)





# The data we need to retreive
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The Winner of the election based on popular vote.

