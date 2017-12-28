#!/usr/bin/python3
#
# Python Assignment #3
# filename: as3.py
#

import sys

#
# 3. Given a list of strings, return a list with the strings in sorted order,
#    except group all the strings that begin with 'x' first.
#    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
#    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']. 
#
# Hint: this can be done by making 2 lists and sorting each of them before combining them.
#
# i. ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
# ii. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
#

lst1 = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
lst2 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']


def sortList(lst):
    result = []
    if type(lst) == list:
        for strg in lst:
            if strg[0].lower() == 'x':
                result.append(strg)

        for strg in result:
            lst.remove(strg)

        lst.sort()
        result.sort()
        result += lst

    return result


print("\nPython Assignment #3")
print("\nList #1")
print("Unsorted: {0}".format(str(lst1)))
print("Sorted:   {0}".format(str(sortList(lst1))))
print("\nList #2")
print("Unsorted: {0}".format(str(lst2)))
print("Sorted:   {0}".format(str(sortList(lst2))))

sys.exit(0)
