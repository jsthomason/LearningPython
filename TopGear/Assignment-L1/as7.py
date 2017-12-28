#!/usr/bin/python3

#
# Python Assignment #7
# filename: as7.py
#

import sys

#
# 7. Given a string... 
str1="""Python is a widely used high-level programming language for general-purpose programming, 
created by Guido van Rossum and first released in 1991. An interpreted language, 
Python has a design philosophy which emphasizes code readability (notably using whitespace 
indentation to delimit code blocks rather than curly braces or keywords), and a syntax 
which allows programmers to express concepts in fewer lines of code than possible in 
languages such as C++ or Java. The language provides constructs intended to enable writing 
clear programs on both a small and large scale. Python features a dynamic type system and 
automatic memory management and supports multiple programming paradigms, including 
object-oriented, imperative, functional programming, and procedural styles. It has a large 
and comprehensive standard library. Python interpreters are available for many operating 
systems, allowing Python code to run on a wide variety of systems. CPython, the reference 
implementation of Python, is open source software and has a community-based development model, 
as do nearly all of its variant implementations. CPython is managed by the non-profit 
Python Software Foundation."""

#
# a. Build a dictionary, with "words as key" --> Frequency of occurrence as value
# E.g. Python: 7, is: 3
# b. Print the top 5 words with their frequency of occurrence
#

def freqOfOccurrence(theStr):
    freqOfOccurrenceDict = {}
    punctuation = '.,()\n '
    for word in theStr.split(' '):
        word = word.lstrip(punctuation).rstrip(punctuation)
        if word in freqOfOccurrenceDict:
            freqOfOccurrenceDict[word] += 1
        else:
            freqOfOccurrenceDict.update({word:1})

    return freqOfOccurrenceDict

def revSortDictByVal(d):
    rs = [[k, d[k]] for k in sorted(d, key=d.get, reverse=True)]
    return rs

print("\nPython Assignment #7\n")

sd = revSortDictByVal(freqOfOccurrence(str1))
for e in range(0,5):
    print("{0} - {1}, is #{2}".format(sd[e][0], sd[e][1], e+1))


sys.exit(0)


