#!/usr/bin/python3
"""
Use program to test the MathNew package.
"""
from sys import path
path.append("./MathNew")

import MathNew

a = 9
b = 3

print("Testing addition module \"add({0},{1})\" = {2}".format(a, b, MathNew.add(a,b)))
print("Testing division module \"div({0},{1})\" = {2}".format(a, b, MathNew.div(a,b)))
print("Testing multiplication module \"mul({0},{1})\" = {2}".format(a, b, MathNew.mul(a,b)))
print("Testing subtration module \"sub({0},{1})\" = {2}".format(a, b, MathNew.sub(a,b)))
print("Testing sqroot module \"sqr({0})\" = {1}".format(a, MathNew.sqr(a)))


