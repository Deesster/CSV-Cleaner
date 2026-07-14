import pandas as pd

# Read CSV file

df = pd.read_csv("input.csv")

# Remove empty rows

df = df.dropna(how="all")

# Remove duplicates

df = df.drop_duplicates()

# Sort by the first column

first_column = df.columns[0]

df = df.sort_values(by=first_column)

# Save cleaned file

df.to_csv("cleaned_output.csv", index=False)

print("CSV file cleaned successfully!")
