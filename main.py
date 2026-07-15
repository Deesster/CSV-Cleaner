import csv

# Read CSV file

with open("input.csv", "r", newline="", encoding="utf-8") as file:

    reader = csv.reader(file)

    rows = [row for row in reader if any(cell.strip() for cell in row)]

# Remove duplicates

unique_rows = []

for row in rows:

    if row not in unique_rows:

        unique_rows.append(row)

# Keep header separate

header = unique_rows[0]

data = unique_rows[1:]

# Sort data by first column

data.sort(key=lambda x: x[0])

# Write cleaned CSV file

with open("cleaned_output.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(header)

    writer.writerows(data)

print("CSV file cleaned successfully!")
