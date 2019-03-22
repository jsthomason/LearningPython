#!/usr/bin/python3
'''
Write a code to compare two string data based on the length of the string hint; __gt__ method
'''

class StrCompare(str):

    def __init__(self, txt):
        #print(self, "Constructor")
        print(self.__class__.__name__, "Constructor:", str(txt))
        if type(txt) == str:
            self.txt = txt
        else:
            raise Exception("variable 'txt' must be type 'str'(string)")

    def __gt__(self, o):
        result = False
        if type(self) == type(o):
            if len(self) > len(o): result = True
        else:
            raise Exception("Object types are not the same; Not Comparable!")
        return result

#~~~~~~~~~~~~~~~~~~~ Test Code ~~~~~~~~~~~~~~~~~~~~~~~#

def main():
    txt1 = "Suzy"
    txt2 = "Bob"

    try:
        sc1 = StrCompare(txt1)
        sc2 = StrCompare(txt2)
        print("length of {} > {} = {}".format(txt1, txt2, (sc1 > sc2)))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()