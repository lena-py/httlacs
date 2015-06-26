__author__ = 'lena'

# Aliasing a list
a = [1, 2, 3]
b = a
a[0] = 5
print(b)

# Aliasing a list means both variables reference the same object
for i in (a, b):
    print(id(i))

# Immutable types are not aliasable...error results from code below
a = "hello"
b = a
a[:] = a[:1]
print(b)
print(a)