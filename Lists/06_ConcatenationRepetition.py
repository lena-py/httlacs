__author__ = 'lena'

# Concatenation operators
fruit = ["apple", "banana", "grapefruit"]
print([1 + 2] + [3 + 4] + [7])
newlist = fruit + [6, 7, 8, 9]

print([0] * 4)
print([1, 2, ["yes", "no"]] * 2)

# Concatenation to create new list creates new object
fruit_id = id(fruit)
newlist_id = id(newlist)
print("Fruit's id is {} while newlist's id is {}".format(fruit_id, newlist_id))
