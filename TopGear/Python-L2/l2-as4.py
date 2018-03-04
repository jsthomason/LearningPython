#!/usr/bin/python3
"""
Python L2 Assignment #4

4.   Write a code to implement the following methods by defining a class called Mymath 
a) with __init__  
    1. sqroot
    2. addition
    3. subtraction
    4. multiplication
    5. division
"""

from math import sqrt

class MyMath:
    """
    MyMath class for Assignment #3
    With Constructor
    """
    def __init__(self):
        print("MyMath Constructor")

    def __del__(self):
        print("MyMath Destructor")

    def add(self,x,y):
        return x + y

    
    def div(self,x,y):
        return x / y


    def mul(self,x,y):
        return x * y


    def sub(self,x,y):
        return x - y


    def sqr(self,x):
        return sqrt(x)


mm = MyMath()

a = 9
b = 3

print("add({0} + {1}) = {2}".format(a, b, mm.add(a,b)))
print("div({0} / {1}) = {2}".format(a, b, mm.div(a,b)))
print("mul({0} x {1}) = {2}".format(a, b, mm.mul(a,b)))
print("sub({0} - {1}) = {2}".format(a, b, mm.sub(a,b)))
print("sqr({0})     = {1}".format(a, mm.sqr(a)))
