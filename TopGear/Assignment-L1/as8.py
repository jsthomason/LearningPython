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
    #
    # Turn the passed string into a list of words; punctuation stripped
    for word in theStr.split(' '):
        word = word.lstrip(punct).rstrip(punct)
        theList.append(word)

    #
    # Iterate 'theList' and build the dictionary(theDict)
    for i in range(0,len(theList)):
        # see if the 'word' is already in the dictionary
        if theList[i] in theDict:
            tmpList = theDict[theList[i]]
            # if we are not at the end of the list...
            if i < (len(theList)-1):
                # if the word is not already in the list...
                if theList[i+1] not in tmpList:
                    # append the next word to the list
                    tmpList.append(theList[i+1])
            # update the dictionary with the new list of words
            theDict[theList[i]] = tmpList
        # if not; add the word(key) to the dictionary using a list as the value
        else:
            if i < (len(theList)-1):
                theDict.update({theList[i]:[theList[i+1]]})

    return theDict

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

results = buildDict(str1)

print("\nPython Assignment #8")

print("\nDict Len: " + str(len(results)))
# iterate over the results printing each word in the dictionary followed by it's list of values
for k, v in results.items():
    print("{0:16}: {1}".format(str(k), str(v)))

sys.exit(0)

