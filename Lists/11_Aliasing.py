__author__ = 'lena'

# Aliasing a list
a = [1, 2, 3]
b = a
a[0] = 5
print(b)

# Strings, ints are not aliasable
a = 1
b = a
a = 2
print(b)