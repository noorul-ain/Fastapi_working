#  Convert CSV File to JSON & Save it as JSON File
import csv 
import json 

with open('output.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    field_names = next(csv_reader)
    data = []
    for row in csv_reader:
        data.append(dict(zip(field_names, row)))

with open('data.json', 'w') as json_file:
    json_data = json.dumps(data)
    json_file.write(json_data)