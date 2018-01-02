#!/usr/bin/python3

#
# Python Assignment #9
# filename: as9.py
#

import sys, re

# 9.  Below is the output of # show ip interface brief command on a router

str1="""
Interface          IP-Address      OK?     Method   Status   Protocol

FastEthernet0/0    192.168.1.242   YES     manual   up       up 
FastEthernet1/0    unassigned      YES     unset    down 
Serial2/0          192.168.1.250   YES     manual   up       up 
Serial3/0          192.168.1.233   YES     manual   up       up 
FastEthernet4/0    unassigned      YES     unset    down    
FastEthernet5/0    unassigned      YES     unset    down
"""
# 
#  a. Use regular expressions to extract and display Interface and method status for all the interfaces.
#  i. E.g.  FastEthernet0/0, manual up

print("\nPython Assignment #9\n")

parser = re.compile('^[F|S].*', re.MULTILINE)
resultList = parser.findall(str1)

interface = re.compile('^[F|S].+\d/\d')
method    = re.compile('(manual|unset)')
status    = re.compile('(up|down)')

for result in resultList:
    print("{0}, {1} {2}".format(interface.search(result).group(), method.search(result).group(), status.search(result).group()))

sys.exit(0)

