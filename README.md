# contactTracing
Just a simple contact tracing script, example files provided.

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
