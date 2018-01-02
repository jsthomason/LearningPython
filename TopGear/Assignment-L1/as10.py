#!/usr/bin/python3

#
# Python Assignment #10
# filename: as10.py
#

import sys

#
# 10. Given a number line from -infinity to +infinity.
# You start at 0 and can go either to the left or to the right.
# The condition is that in i’th move, you take i steps.
# In the first move take 1 step, second move 2 steps and so on. 
# 
# Hint:
#      3 can be reached in 2 steps (0, 1) (1, 3).
#      2 can be reached in 3 steps (0, 1) (1,-1) (-1, 2)
#
# a) Find the optimal number of steps to reach position 1000000000 and -1000000000. 
#

print("\nPython Assignment #10\n")


def find(x):
    r = 0
    i = 0
    s = 0
    while r != x:
        s += 1
        if r < x:
            i += 1
            r += abs(i)
        elif r > x:
            i -= 1
            r -= abs(i)

    return s

var1=1000000000
var2=-1000000000

print("Steps: {0} to reach {1}".format( str(find(var1)), str(var1) ))
print("Steps: {0} to reach {1}".format( str(find(var2)), str(var2) ))

sys.exit(0)
