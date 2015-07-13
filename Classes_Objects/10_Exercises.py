__author__ = 'lena'
import math

# Add a distanceFromPoint method that works similar to distanceFromOrigin
# except that it takes a Point as a parameter
# and computes the distance between that point and self.


class Point():
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y

    def __str__(self):
        return str("x = {}, y = {}".format(str(self.x), str(self.y)))

    def distance_from_point(self, target):
        x_difference = math.fabs(self.x - target.x)
        y_difference = math.fabs(self.y - target.y)
        return "The distance between two points is: {:.2f}".format(((x_difference ** 2) + (y_difference ** 2)) ** 0.5)

# Add a method reflect_x to Point which returns a new Point,
#   one which is the reflection of the point about the x-axis.
#   For example, Point(3, 5).reflect_x() is (3, -5)

    def reflect_x(self):
        new_x = 0 - self.x
        return Point(new_x, self.y)

point_1 = Point(0, 0)
point_2 = Point(10, 10)

print(point_1.distance_from_point(point_2))
print(point_2.reflect_x())


