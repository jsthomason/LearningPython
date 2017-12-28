#!/usr/bin/python3

#
# Python Assingment #4
# filename: as4.py
#

import sys

#
# 4. Given a list of non-empty tuples, return a list sorted in increasing 
#    order by the last element in each tuple. 
#    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields 
#         [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
#
#    Hint: use a custom key= function to extract the last element form each tuple.
#       i.  [(1, 3), (3, 2), (2, 1)]
#       ii. [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
# 

lst1 = [(1, 3), (3, 2), (2, 1)]
lst2 = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

def sortList(lst):
    lst.sort(key=lambda element: element[-1])
    return lst

print("\nPython Assignment #4")

print("\nList #1")
print("Unsorted: {0}".format(str(lst1)))
print("Sorted:   {0}".format(str(sortList(lst1))))

print("\nList #2")
print("Unsorted: {0}".format(str(lst2)))
print("Sorted:   {0}".format(str(sortList(lst2))))


sys.exit(0)
