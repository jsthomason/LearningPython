#!/usr/bin/python3
"""
Python L2 Assignment #2

2.  Given email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'
write a regular  expression to extract 
a. email id
b. domain name
c. time
"""

import re
from sys import exit

email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'

em = re.compile(r"[a-z]+\..*@.*\.[a-z]+")
dn = re.compile(r"(?<=@).*\.[a-z]+")
tm = re.compile(r"\d+:\d+:\d+")

print("a. email id:    {0}".format( em.search(email).group() ))
print("b. domain name: {0}".format( dn.search(email).group() ))
print("c. time:        {0}".format( tm.search(email).group() ))


exit(0)
