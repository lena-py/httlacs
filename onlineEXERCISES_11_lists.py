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


# ACCESSING ELEMENTS
print('---ACCESSING ELEMENTS---')
"""
use index operator
"""
numbers = [4, 'cat', 376, 2*10, 0, -12, len('sgt')]
print(numbers[2])
print(numbers[9-8])
print(numbers[-2])
print(numbers[len(numbers)-1])
"""
successive indices
"""
print(numbers[1].upper()[0] + numbers[1][1:])

# CONCATENATION AND REPETITION
print('---CONACATENATION AND REPETITION---')
fruit = ['apples', 'bananas', 'guanabanas', 'pears', 'candy']
print([1, 2] + [3, 4])
print(fruit + [6, 7, 8, 9])

print([0] * 4)
print([1, 2, ['hello', 'goodbye']] * 2)

""" id is the unique identifier for objects corresponding to an address in memory"""
print(id(fruit))




