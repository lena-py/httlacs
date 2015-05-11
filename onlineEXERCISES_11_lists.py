# LIST VALUES

"""
we can also assign list values to variables and pass lists as parameters to functions.
"""
import math


def power(y):
    return math.pow(10, y)

a = [10, 20, 30, [30, 40]]
print(power(a[0]))


