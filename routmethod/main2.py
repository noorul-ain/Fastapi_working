
import json 
import csv 

# Read data from JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Assuming data is a list of dictionaries, you can modify this depending on your JSON structure
if isinstance(data, list) and data:
    fieldnames = data[0].keys()  # Extract field names from the first dictionary in the list
    with open('data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write rows
        for row in data:
            writer.writerow(row)
    print("Conversion successful: JSON to CSV.")
else:
    print("No data found or data format is incorrect.")

