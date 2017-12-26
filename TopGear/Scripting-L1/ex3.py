#!/usr/bin/python3
#
# Exercise #3
# filename: ex3.py
#

import sys, os

# Implement the function isListOfInts(), which takes a list, and checks if the list has
# only "int" type values, as per the specification given below:
#     • The function should return True, if the list has only "int" type values, otherwise
#       should return False.
#     • The function should return True, if an empty list is passed as argument.
#     • If the argument is not of ‘list’ type, then the function should throw ValueError
#       exception, with the error message 'arg not of <list> type'
#     • The function should have only one return statement.
#
##########################################################################################
def isListOfInts(l):
    result = True
    if type(l) == list:
        if len(l) == 0:
            result = True
        else:
            for item in l:
                if type(item) == int: continue
                else: 
                    result = False
                    break

        return result

    else:
        raise ValueError(l)

#
# testList(l)
# Pass an object to test if it is an Integer List
##########################################################################################
def testList(l):
    try:
        print(str(l) + " --> " + str(isListOfInts(l)))

    except ValueError as e:
        print("ValueError: " + str(e.args[0]) + " - is not of <list> type\n")



#     To test correctness of the function isListOfInts(),implement the function testList()
#     which is called as shown below and should produce output as indicated.
###########################################################################################
testList([])
testList([1])
testList([1,2])
testList([0])
testList(['1'])
testList([1,'a'])
testList(['a',1])
testList([1,1.0])
testList([1.0,1.0])
testList((1,2))

sys.exit

