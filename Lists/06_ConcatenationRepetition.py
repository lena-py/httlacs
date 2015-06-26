__author__ = 'lena'

# Concatenation operators
fruit = ["apple", "banana", "grapefruit"]
print([1 + 2] + [3 + 4] + [7])
newlist = fruit + [6, 7, 8, 9]
print(newlist)

print([0] * 4)
print([1, 2, ["yes", "no"]] * 2)

cloned_list = fruit[:]
aliased_list = fruit

# Concatenation and the slice operator to create new list creates new object...
# ...but using assignment operator aliases
fruit_id = id(fruit)
newlist_id = id(newlist)
cloned_list_id = id(cloned_list)
aliased_list_id = id(aliased_list)
print("Fruit's id is {} while newlist's id is {}. "
      "Cloned_list's id is {} but aliased_list is {}".format(fruit_id, newlist_id, cloned_list_id, aliased_list_id))
