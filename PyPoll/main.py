# Import variables
import csv
import os

# Create variables to store data
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Files to load and output 
csv_file = os.path.join("Resources", "election_data.csv")  
analysis_file = os.path.join("analysis", "election_analysis.txt")

#Open and read csv file
with open(csv_file, "r") as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Loop through each row in the csv file
    for row in csv_reader:
        total_votes +=1
        candidate_name = row[2]
        
        if candidate_name in candidates:
            candidates[candidate_name] +=1
        else:
            candidates[candidate_name] = 1
            
# Initialize variable for results
results = []

# Get percentage of candidate votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))
    
# Determine winner
for candidate, votes, percentage in results:
    if votes > max_votes:
        max_votes = votes
        winner = candidate
        
# Generate the output summary
output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
)

for candidate, votes, percentage in results:
    output += f"{candidate}: {percentage: .3f}% ({votes})\n"
    
output += (
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(analysis_file, "w") as txt_file:
    txt_file.write(output)



