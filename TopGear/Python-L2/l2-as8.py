#!/usr/bin/python3
'''
Assignment #8
Create a class called Circle and write the methods to calculate the area and circumference of a circle given the radius.
'''

from math import pi

class Circle(object):

    def area(self, radius):
        return (pi*(radius**2))

    def circumference(self, radius):
        return (2*pi*radius)


#~~~~~~~~~~~~~~~~~ Test Code ~~~~~~~~~~~~~~~~~~~~~

def main():

    radius = 3
    c = Circle()
    print("Area of a Circle with the radius of {} = {:0.3f}".format(radius, c.area(radius)))
    print("Circumference of a Circle with the radius of {} = {:0.3f}".format(radius, c.circumference(radius)))
    return

if __name__ == "__main__":
    main()