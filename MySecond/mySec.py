import math

class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def __del__(self):
        del self

    def X(self,x=0):
        if x:
            self.x = x
        return self.x

    def Y(self,y=0):
        if y:
            self.y = y
        return self.y

class Circle(Point):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def center(self):
        return "(" + str(self.X()) + "," + str(self.Y()) + ")"


c = Circle(5,6)

print(c.center())


