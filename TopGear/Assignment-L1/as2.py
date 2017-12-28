#!/usr/bin/python3
#
# Python Assignment #2
# filename: as2.py
#

import sys

#
# 2. Given a list of strings, return the count of the number of strings where 
#    the string length is 2 or more and the first and last chars of 
#    the string are the same.  
#
# i. ['axa', 'xyz', 'gg', 'x', 'yyy']
# ii. ['x', 'cd', 'cnc', 'kk']
# iii. ['bab', 'ce', 'cba', 'syanora']
#

lst1 = ['axa', 'xyz', 'gg', 'x', 'yyy']
lst2 = ['x', 'cd', 'cnc', 'kk']
lst3 = ['bab', 'ce', 'cba', 'syanora']


def tstStr(lst):
    cnt = 0
    for strg in lst:
        if len(strg) >= 2: 
            if strg[0] == strg[-1]: cnt += 1

    return cnt


print("\nPython Assignment #2\n")
print("{0}\nCount: {1}\n".format(str(lst1), tstStr(lst1)))
print("{0}\nCount: {1}\n".format(str(lst2), tstStr(lst2)))
print("{0}\nCount: {1}\n".format(str(lst3), tstStr(lst3)))

sys.exit(0)
