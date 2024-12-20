import csv

# Read the CSV file
file_path = "C:/Users/ernes/Homework/03-Python/python-challenge/PyBank/Resources/budget_data.csv"
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    data = list(csvreader)

# Initialize variables
total_months = 0
net_total = 0
changes = []
dates = []

# Calculate total number of months, net total, changes, and dates
for i in range(len(data)):
    total_months += 1
    net_total += int(data[i][1])
    if i > 0:
        change = int(data[i][1]) - int(data[i-1][1])
        changes.append(change)
        dates.append(data[i][0])

# Calculate average change
average_change = round(sum(changes) / len(changes), 2)

# Find greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
