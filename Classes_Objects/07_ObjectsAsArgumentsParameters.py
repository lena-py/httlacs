__author__ = 'lena'
import math

# Create a class for coordinates


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """Create a new point at the origin. """
        self.x = initX  # attribute
        self.y = initY  # another attribute

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)

    return dist

p = Point(7, 9)
q = Point(0, 0)

print("Distance: {:.2f}".format(distance(p, q)))