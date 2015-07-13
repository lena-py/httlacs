__author__ = 'lena'
import math

# Create a class for coordinates


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """Create a new point. """
        self.x = initX  # attribute
        self.y = initY  # another attribute

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(str(self.x), str(self.y))

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)

    return dist

p = Point(10, 10)
q = Point(0, 0)

mid = p.halfway(q)
print(mid)
print(mid.getX())
print(mid.getY())

