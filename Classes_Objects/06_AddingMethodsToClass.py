__author__ = 'lena'

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


p = Point(7, 9)
q = Point(0, 0)
q.y = 12

print(q.distanceFromOrigin())