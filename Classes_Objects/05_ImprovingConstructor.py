__author__ = 'lena'

# Create a class for coordinates


class Point:
    """ Point class for representing and manipulating x,y coordinates. """


    def __init__(self, initX, initY):
        """Create a new point at the origin. """
        self.x = initX  # attribute
        self.y = initY  # another attribute

p = Point(7, 9)
q = Point(0, 0)

print(id(p), id(q))