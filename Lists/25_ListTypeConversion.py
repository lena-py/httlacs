__author__ = 'lena'

# Each letter becomes an elem in a lst
xs = list("Crunchy Frog")
print(xs)

# Each int becomes an elem in a lst
xs = list(range(10))
print(xs)

# Only works on iterable items
try:
    xs = list(135)
except TypeError:
    print("***TypeError: int not iterable***")

