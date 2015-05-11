# LIST VALUES
"""
we can also assign list values to variables and pass lists as parameters to functions.
"""
import math

def power(y):
    return math.pow(10, y)

mixed_list = ["hello world", 10*2, [10, 2]]
a = [10, 20, 30, [30, 40]]
new_list = [mixed_list, a]
# print(power(a[0]))
# print(mixed_list)
# print(new_list)


# LIST LENGTH
print(len(mixed_list))
print(len(a))
print(len(new_list))
# prints the uppercase of the first list item, but only the first 5 characters
print(mixed_list[0].upper()[0:1+4])


# LIST MEMBERSHIP
print("hello world" in mixed_list)
print("hello" in mixed_list)
print("hello" not in mixed_list)
print(40 in a)
print(2 in mixed_list)



