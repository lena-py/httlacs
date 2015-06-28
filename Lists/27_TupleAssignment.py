__author__ = 'lena'

# Var on left side can be assigned to tuple on right
cat = ("domestic shorthair", "black", 17, "sammy")
(breed, color, age, name) = cat
print(breed, color, age, name)

# Swap values (right side of statement evaluated before assigned to left side)
a = 12
b = 0
(a, b) = (b, a)
print(a, b)

# Must have same num of var on left must match vlus on right
c = 15
try:
    (a, b, c) = (b, a)
except ValueError:
    print("You've got an error")