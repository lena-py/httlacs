__author__ = 'lena'

# Create a list of where the sublists == parent list
orig_list = [1, 3, 5]
new_lst1 = [orig_list] + [orig_list]
new_lst2 = [orig_list] * 2
print(orig_list * 2)    # without list operator the elements are repeated within the original index
print(new_lst1)
print(new_lst2)

# Lists made this way create new objects...
for i in (orig_list, new_lst1, new_lst2):
    print(id(i))

# ...but the elements are references to the same object: orig_list
for i in range(len(new_lst1)):
    print(id(new_lst1[i]))
    print(id(new_lst2[i]))

# Because of this, replacing the elements in the orig_list changes the "linked" lists
orig_list[:] = [2, 4, 7]
print(new_lst1)
print(new_lst2)

# Why does this create a new object?
# I think because just above we are replacing elements of an existing object...
# ... but below we are using the assignment operator which creates a new object
print(id(orig_list))
orig_list = [1, 3, 5]
print(id(orig_list))
print(new_lst1)
print(new_lst2)

# Elements of the lists are still pointing to original object...
# ...and thus are unchanged by the reassignment of the parent
for i in range(len(new_lst1)):
    print(id(new_lst1[i]))
    print(id(new_lst2[i]))

# Changing an element that is a reference copied from the parent
# does not change other elements that are pointing to the same parent
new_lst1[1] = 69
print(new_lst2)
for i in range(len(new_lst1)):
    print(id(new_lst1[i]))
    print(id(new_lst2[i]))

# Because line 29 above creates a new object, further changes to this object affect only itself
# and the sublists are still referencing the original object as it was before the reassignment.
# Lesson learned: variable reassignment can be dangerous
orig_list[:] = [12]
print(new_lst2)
print(new_lst1)
