#!/usr/bin/python3
# Strings
'''Is this a doc string???'''

PF = 'JKLMNOPQ'
SF = 'ack'

for l in PF:
    if l == 'O' or l == 'Q':
        print(l + 'u' + SF)
    else:
        print(l + SF)
