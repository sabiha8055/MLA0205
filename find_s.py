# ============================================================
# PRACTICAL PROBLEM 1: FIND-S ALGORITHM
# ============================================================

import csv

# ------------------------------------------------------------
# STEP 1: Create the EnjoySport CSV file
# ------------------------------------------------------------

data = [
    ["Sky", "AirTemp", "Humidity", "Wind", "Water", "Forecast", "EnjoySport"],
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]

with open("enjoysport.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("EnjoySport CSV file created successfully!")

# ------------------------------------------------------------
# STEP 2: Read the CSV file
# ------------------------------------------------------------

with open("enjoysport.csv", "r") as file:
    reader = csv.reader(file)

    # Convert CSV data into a list
    data = list(reader)

# First row contains attribute names
attributes = data[0]

# Remaining rows are training examples
training_data = data[1:]

print("\nAttributes:")
print(attributes)

print("\nTraining Data:")
for row in training_data:
    print(row)

# ------------------------------------------------------------
# STEP 3: FIND-S Algorithm
# ------------------------------------------------------------

# Number of attributes (excluding EnjoySport)
num_attributes = len(attributes) - 1

# Start with the most specific hypothesis
hypothesis = ["0"] * num_attributes

print("\nInitial Hypothesis:")
print(hypothesis)

# Examine each training example
for i, row in enumerate(training_data):

    # Last column is the target value
    target = row[-1]

    # Consider only positive examples
    if target.lower() == "yes":

        for j in range(num_attributes):

            # If hypothesis is empty, copy the value
            if hypothesis[j] == "0":
                hypothesis[j] = row[j]

            # If values are different, replace with ?
            elif hypothesis[j] != row[j]:
                hypothesis[j] = "?"

    print("\nHypothesis after training example", i + 1, ":")
    print(hypothesis)

# ------------------------------------------------------------
# STEP 4: Display Final Answer
# ------------------------------------------------------------

print("\n======================================")
print("FINAL MOST SPECIFIC HYPOTHESIS")
print("======================================")
print(hypothesis)
