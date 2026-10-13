import csv

file_path = r"D:\Coding\Practice\CSV\sample_data.csv"
output_path = r"D:\Coding\Practice\CSV\cleaned_data.csv"

# Read the CSV file
with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames   # save the header
    data = list(reader)

if not data:
    print("No data rows found in the input file. Nothing to clean.")
    raise SystemExit

cleaned_data = []

# Clean the data
for row in data:
    row["name"] = row["name"].strip()
    row["city"] = row["city"].strip()
    row["email"] = row["email"].strip().lower()

    # Remove duplicate records
    if row not in cleaned_data:
        cleaned_data.append(row)

# Write the cleaned data to a new CSV file
with open(output_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_data)

# Print the summary
print("CSV cleaning completed!")
print("Original records:", len(data))
print("Cleaned records:", len(cleaned_data))
print("Duplicate records removed:", len(data) - len(cleaned_data))
print("Output file:", output_path)
