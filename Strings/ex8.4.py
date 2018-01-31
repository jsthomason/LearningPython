#!/usr/bin/python3
"""
# Strings
# Find Function modifed
"""

# find function
def find(word, letter, index=0):
    """
    find() -- find func
    """
    while index < len(word):
        if word[index] == letter:
            return index
        else: index += 1

    return -1


print(find("Thomason", 'o', 1))


