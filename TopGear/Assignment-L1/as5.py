#!/usr/bin/python3

#
# Python Assignment #5
# filename: as5.py
#

import sys

# 5. Given a list of numbers, return a list where all adjacent == elements 
#    have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3].
#
# You may create a new list or modify the passed in list.
# i.  [1, 2, 2, 3]
# ii. [2, 2, 3, 3, 3]
#


class myList(list):

    def uniq(self, lst):
        lst.sort()
        uniq_lst = []
        for e in range(0,len(lst)):
            if lst[e] != lst[e - 1]: uniq_lst.append(lst[e])

        return uniq_lst

lst1 = [1, 2, 2, 3]
lst2 = [2, 2, 3, 3, 3]
lst3 = [2, 3, 3, 2, 3, 4, 7, 4, 7]

print("\nPython Assignment #5")

ml = myList()

print("\nOriginal List: {0}".format(str(lst1)))
print("Unique List:   {0}\n".format(str(ml.uniq(lst1))))

print("\nOriginal List: {0}".format(str(lst2)))
print("Unique List:   {0}\n".format(str(ml.uniq(lst2))))

print("\nOriginal List: {0}".format(str(lst3)))
print("Unique List:   {0}\n".format(str(ml.uniq(lst3))))

sys.exit(0)
