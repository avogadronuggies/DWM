import csv

# Initialize data
data = [
    ['1', 'Red', 'Sports', 'Domestic', 'Yes'],
    ['2', 'Red', 'Sports', 'Domestic', 'No'],
    ['3', 'Red', 'Sports', 'Domestic', 'Yes'],
    ['4', 'Yellow', 'Sports', 'Domestic', 'No'],
    ['5', 'Yellow', 'Sports', 'Imported', 'Yes'],
    ['6', 'Yellow', 'Suv', 'Imported', 'No'],
    ['7', 'Yellow', 'Suv', 'Imported', 'Yes'],
    ['8', 'Yellow', 'Suv', 'Domestic', 'No'],
    ['9', 'Red', 'Suv', 'Imported', 'No'],
    ['10', 'Red', 'Sports', 'Imported', 'Yes'],
]

# Optional: Write data to a CSV file
with open("vehicle_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Calculate probabilities for each attribute
ProbRed = len([row for row in data if row[1] == 'Red']) / len(data)
ProbYellow = len([row for row in data if row[1] == 'Yellow']) / len(data)
ProbYes = len([row for row in data if row[4] == 'Yes']) / len(data)
ProbNo = len([row for row in data if row[4] == 'No']) / len(data)
ProbSuv = len([row for row in data if row[2] == 'Suv']) / len(data)
ProbSports = len([row for row in data if row[2] == 'Sports']) / len(data)
ProbDomes = len([row for row in data if row[3] == 'Domestic']) / len(data)
ProbImported = len([row for row in data if row[3] == 'Imported']) / len(data)

# Conditional probabilities
ProbYesRed = len([row for row in data if row[1] == 'Red' and row[4] == 'Yes']) / len([row for row in data if row[1] == 'Red'])
ProbRed_Yes = ProbYesRed * ProbRed / ProbYes

ProbYesSuv = len([row for row in data if row[2] == 'Suv' and row[4] == 'Yes']) / len([row for row in data if row[2] == 'Suv'])
ProbSuv_Yes = ProbYesSuv * ProbSuv / ProbYes

ProbYesDomes = len([row for row in data if row[3] == 'Domestic' and row[4] == 'Yes']) / len([row for row in data if row[3] == 'Domestic'])
ProbDom_Yes = ProbYesDomes * ProbDomes / ProbYes

# Probability for the new tuple X = { Color: Red, Type: SUV, Origin: Domestic }
ProbX_Yes = ProbRed_Yes * ProbSuv_Yes * ProbDom_Yes
ProbX_No = (1 - ProbRed_Yes) * (1 - ProbSuv_Yes) * (1 - ProbDom_Yes)

# Display the dataset
print("--------------------- Dataset ---------------------")
print("The dataset is:")
for row in data:
    print(row)

# Print dataset dimensions
print("------- Dataset Dimensions -------")
print("No. of Rows:", len(data))
print("No. of Columns:", len(data[0]))

# Print individual class probabilities for "Yes" and "No"
print("----- Individual Class Probabilities (Stolen = Yes) -----")
print("P(Red | Yes):", ProbRed_Yes)
print("P(SUV | Yes):", ProbSuv_Yes)
print("P(Domestic | Yes):", ProbDom_Yes)

print("----- Individual Class Probabilities (Stolen = No) -----")
print("P(Red | No):", 1 - ProbRed_Yes)
print("P(SUV | No):", 1 - ProbSuv_Yes)
print("P(Domestic | No):", 1 - ProbDom_Yes)

# Print overall probabilities for attributes
print("----- Overall Attribute Probabilities -----")
print("P(Red):", ProbRed)
print("P(Yellow):", ProbYellow)
print("P(SUV):", ProbSuv)
print("P(Sports):", ProbSports)
print("P(Domestic):", ProbDomes)
print("P(Imported):", ProbImported)
print("P(Yes):", ProbYes)
print("P(No):", ProbNo)

# Display classification results
print("----- Classification for New Tuple X = { Color: Red, Type: SUV, Origin: Domestic } -----")
print("The Probability of X | Stolen = Yes is:", ProbX_Yes)
print("The Probability of X | Stolen = No is:", ProbX_No)
print("Classification Result:", "YES" if ProbX_Yes > ProbX_No else "NO")
