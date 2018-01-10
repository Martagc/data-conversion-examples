vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "kale"},
 {"name": "squash"},
 {"name": "brocoli"},
 {"name": "cauliflower"},
]

print(vegetables)

import csv

with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'length']) 
	for veggie in vegetables:
		#I want the name of the vegetable
		vegetable_name = veggie['name']
		#I want the length of the vegetable name
		vegetable_name_length = len(vegetable_name)
		#write those to csv
		row = [vegetable_name, vegetable_name_length]
		writer.writerow(row)