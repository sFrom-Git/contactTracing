"""
This script takes a text file in the following format:

Starting with:
- a number that represents the meeting number

followed by:
- a space separated line of names

ending in:
- a newline character

AND

At least one of the names must have an asterisk '*' next to it to signify
the initial infected person:

e.g.

1 Harry Fred John Paul Mark
2 Fred *Mark Fran Trent Bill
3 Jeff John Donald Fran Ray Frank Fred Julie Sarah

The script will print the names of all the people who have had 
contact with an infected person (the order of the names signifies
seating plans in the room, if you are seated next to an infected person
you will be considered infected) at each meeting.

e.g. the output from the above input:

2 Mark Fred Fran 3
3 Mark Fred Fran Frank Julie Donald Ray 7

The script also will print the number of infected in that meeting
at the end of the line.

Example files to test this script on:
'meetings1.txt'
'meetings2.txt'
'meetings3.txt'

"""

import re

def findInfected(path):
	f1 = open(path)

	infected = []

	line = f1.readline()
	while line != '':
		line = line.split()
		people = []

		if infected == []:
			for i in range(len(line)):
				if re.search('\*', line[i]):
					line[i] = line[i].replace('*', '')
					infected.append(line[i])

		if infected != []:
			for i in range(len(infected)):
				if line.count(infected[i]):

					infectedPosition = line.index(infected[i])

					if infectedPosition == 1:
						if not infected.count(line[infectedPosition + 1]):
							infected.append(line[infectedPosition + 1])
						if not infected.count(line[-1]):
							infected.append(line[-1])

					elif infectedPosition == len(line) - 1:
						if not infected.count(line[1]):
							infected.append(line[1])
						if not infected.count(line[infectedPosition - 1]):
							infected.append(line[infectedPosition - 1])

					else:
						if not infected.count(line[infectedPosition - 1]):
							infected.append(line[infectedPosition - 1])
						if not infected.count(line[infectedPosition + 1]):
							infected.append(line[infectedPosition + 1])

			print(line[0], ' '.join(infected), len(infected))

		line = f1.readline()
	f1.close()



path = None
while path != '':

	print('\n(enter an empty line to terminate.)')
	path = input('Enter file name: ')
	print()

	try:
		if path != '':
			findInfected(path)

	except FileNotFoundError:
		print('File with name \'', path, '\' can not be found', sep='')
		print('Please try again.')
