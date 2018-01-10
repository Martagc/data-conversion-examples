#read superhero.json
import json
from pprint import pprint

with open('superhero.json') as f:
	data = json.load(f)

#selec the members 
members = data['members']	

# Write header to csv
import csv

with open('members.csv', 'w') as f:
	writer = csv.writer(f)
	header = [
		'name',
		'age',
		'secretIdentity',
		'powers',
		'squadName',
		'homeTown',
		'formed',
		'secretBase',
		'active']
	writer.writerow(header)

# Loop over members
	for m in members:
	#for each member, get the row
		row = [
			m['name'],
			m['age'],
			m['secretIdentity'],
			str(m['powers']),
			data['squadName'],
			data['homeTown'],
			data['formed'],
			data['secretBase'],
			data['active']
		]
		writer.writerow(row)

