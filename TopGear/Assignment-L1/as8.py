#!/usr/bin/python3

#
# Python Assignment #8
# filename: as8.py
#

import sys

# 8. Given a string...
str1 = """Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""

# Hint:  Assume that the first word is preceded by " "
# a. Build a dictionary where the key is a word and the value is the list of words that are likely to follow.
# i. E.g. Python  [is, has, features, interpreters, code, Software].
# In this example the words listed are likely to follow “Python”
# b. Given a word predict the word that’s likely to follow.

def buildDict(theStr):
    theDict = {}
    theList = []
    punct = '., \n()'
    for word in theStr.split(' '):
        word = word.lstrip(punct).rstrip(punct)
        theList.append(word)

    for i in range(0,len(theList)):

        #if word in theDict:
        #    tmpLst = theDict.get(word)
        #    tmpLst.append(word)
        #    theDict[word] = tmpLst
        #else:
        #    theDict.update({word:[word]})

    return theList

print("\nPython Assignment #8")

#print("\n{0}".format(str1))
print("{0}".format(str(buildDict(str1))))


sys.exit(0)
