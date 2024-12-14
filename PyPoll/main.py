import csv
file_path = ("Resources/election_data.csv")
# Initialize variables
total_votes = 0
candidates = []
candidate_votes = {}

# Read the CSV file
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
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
output_file = "Election_Analysis.txt"
with open(output_file, 'w') as file:
    file.write("Election_Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total_Votes: {total_votes}")
print("Analysis results have been exported to election_analysis.txt")



