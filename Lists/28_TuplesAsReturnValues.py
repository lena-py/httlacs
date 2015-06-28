__author__ = 'lena'

# Function return value can be a tuple
import math


def circle_info(r):
    # Return the area and circumference of a circle
    c = 2 * math.pi * r
    a = math.pi * r * r
    return c, a

radius = 10
circum = circle_info(radius)[0]
area = circle_info(radius)[1]

print("The circumference of radius {} is {:.2f} and the area is {:.2f}".format(radius, circum, area))


