import csv

# Read the CSV file
file_path = "C:/Users/ernes/Homework/03-Python/python-challenge/PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = []
candidate_votes = {}

# Open the CSV file
with open(file_path) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row

    # Process each row in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_file = "election_analysis.txt"
with open(output_file, 'w') as file:
    file.write("Election Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"Candidate Votes: {candidate_votes}\n")
    file.write(f"Winner: {winner}\n")
    
