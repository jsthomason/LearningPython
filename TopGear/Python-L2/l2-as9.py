#!/usr/bin/python3
'''
Assignment #9
Write a class called Circle and write the methods to calculate the area and circumference of the circle by initialing the radius of the circle.
Hint __init__ method
'''

from math import pi

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (pi*(self.radius**2))

    def circumference(self):
        return (2*pi*self.radius)


#~~~~~~~~~~~~~~~~~ Test Code ~~~~~~~~~~~~~~~~~~~~~

def main():

    radius = 3
    c = Circle(radius)
    print("Area of a Circle with the radius of {} = {:0.3f}".format(radius, c.area()))
    print("Circumference of a Circle with the radius of {} = {:0.3f}".format(radius, c.circumference()))
    return

if __name__ == "__main__":
    main()