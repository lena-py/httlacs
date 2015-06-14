# Create lists
list1 = [1, 2, 3]
print(list1)

# Nested list
list2 = ["hello", "cats are annoying sometimes", "6*2", list1]
print(list2)

# Empty list
list3 = []

# Assign list value to variable
newvar = list2[0]
print(newvar)

# Pass list as parameter to function
def smpl(lst):
    print(lst)

smpl(list2)