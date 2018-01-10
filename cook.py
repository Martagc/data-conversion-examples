#Read csv

import csv
import json

with open('vegetables.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    print(row)

# Writing a json file
with open('vegetables.json', 'w') as f:
	json.dump(rows, f)