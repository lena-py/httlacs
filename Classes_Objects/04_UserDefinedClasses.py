__author__ = 'lena'

# Create a class for coordinates


class Point:
    """ Point class for representing and manipulating x,y coordinates. """


    def __init__(self):
        """Create a new point at the origin. """
        self.x = 0  # attribute
        self.y = 0  # another attribute

p = Point()
q = Point()

print(id(p), id(q))