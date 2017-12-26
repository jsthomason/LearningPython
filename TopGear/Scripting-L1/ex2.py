#!/usr/bin/python3
#
# Exercise - 2
# filename: ex2.py
#

import re, sys, os

# Implement the function isWhiteLine(), which takes a string and returns TRUE if the
# string contains only white space & tab characters.
#####################################################################################
def isWhiteLine(s):
    if re.search(r'^\s*$', s): return True
    else: return False

#
# usage() :: Display script usage
#####################################################################################
def usage():
    print("\nUsage: " + sys.argv[0] + " <filename>\n")


# Making use of the above function, write a program, which should read a file given as
# command-line argument, and print only non-blank lines onto the standard output
######################################################################################

if len(sys.argv) > 1:
    try:
        f = open(sys.argv[1], 'r')
        for line in f:
            if not isWhiteLine(line): print(line, end='')
        f.close()

    except OSError:
        print("\nFile \"" + sys.argv[1] + "\" does not exist...\n")

else:
    usage()

sys.exit
