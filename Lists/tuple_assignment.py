__author__ = 'lena'

# Example 1: assign multiple variables at once
cat = ("domestic shorthair", "black", 17, "sammy")
(breed, color, age, name) = cat
print(breed, color, age, name)

# Example 2: value swapping
a = 12
b = 0
(a, b) = (b, a)
print(a, b)
