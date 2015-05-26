__author__ = 'lena'
import math


def circle_info(r):
    # Return the area and circumference of a circle
    c = 2 * math.pi * r
    a = math.pi * r * r
    return c, a

radius = 10
circum = circle_info(radius)[0]
area = circle_info(radius)[1]

print("The circumference of radius", "{0:.0f}".format(radius), "is", "{0:.2f}".format(circum),
      "and the area is", "{0:.2f}".format(area))


