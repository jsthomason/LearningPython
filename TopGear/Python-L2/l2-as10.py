#!/usr/bin/python3
'''
Create a class called First and two classes called Second and Third which inherit from First.
Create class called Fourth which inherits from Second and Third.
Create a common method called method1 in all the classes and provide the Method Resolution Order
'''
import sys

class First(object):
    def __init__(self):
        print(self.__class__.__name__, "Constructor")

    def method1(self):
        print("{}: {}".format(self.__class__.__name__,  sys._getframe(0).f_code.co_name))

    def meth1(self):
        print("In Class First; Called from class: {}: {}".format(self.__class__.__name__,  sys._getframe(0).f_code.co_name))

class Second(First):
    def __init__(self):
        print(self.__class__.__name__, "Constructor")

    def method1(self):
        print("{}: {}".format(self.__class__.__name__,  sys._getframe(0).f_code.co_name))

    def meth2(self):
        print("In Class Second; Called from class: {}: {}".format(self.__class__.__name__,  sys._getframe(0).f_code.co_name))

class Third(First):
    def __init__(self):
        print(self.__class__.__name__, "Constructor")

    def method1(self):
        print("{}: {}".format(self.__class__.__name__,  sys._getframe(0).f_code.co_name))

    def meth3(self):
        print("In Class Thrid; Called from class: {}: {}".format(self.__class__.__name__,  sys._getframe(0).f_code.co_name))

class Fourth(Second, Third):
    def __init__(self):
        print(self.__class__.__name__, "Constructor")

    def method1(self):
        print("{}: {}".format(self.__class__.__name__,  sys._getframe(0).f_code.co_name))

    def meth4(self):
        print("In Class Fourth; Called from class: {}: {}".format(self.__class__.__name__,  sys._getframe(0).f_code.co_name))


#~~~~~~~~~~~~~~~~~~~~~~~~~ Test Code ~~~~~~~~~~~~~~~~~~~~~~~#
def main():

    a = First()
    b = Second()
    c = Third()
    d = Fourth()

    print()

    # this show method overriding better...
    a.method1()
    b.method1()
    c.method1()
    d.method1()

    print()

    # This shows order better...
    d.meth1()
    d.meth2()
    d.meth3()
    d.meth4()

    return

if __name__ == "__main__":
    main()