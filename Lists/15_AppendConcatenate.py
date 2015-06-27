__author__ = 'lena'

# use the built-in append method of list objects
newlist = list([1, 3, 6])
newlist.append(10)
vlus = (5, 15)
newlist.append(vlus[0])
print(newlist)

# Insert method
newlist.insert(1, vlus[1])
print(newlist)

# Count method
print(newlist.count(5))

# Index method
print(newlist.index(10))

# Reverse method
newlist.reverse()
print(newlist)

# Sort method
newlist.sort()
print(newlist)

# Remove method
newlist.remove(5)
print(newlist)

# Pop method
popitem = newlist.pop(0)
lastitem = newlist.pop()
print(popitem, lastitem)
print(newlist)

# Don't assign list to method that returns None!
badlist = newlist.sort()
print(badlist)


# APPEND VS. CONCATENATE
print('---APPEND VS. CONCATENATE---\n'
      '--- use append to add an item to the end of a list\n'
      '--- use accumulator operation to create a new list and append the item')
example = ["newlist.append(55)", "newlist = newlist + ['cantankerous']"]
for i in range(len(example)):
    print(id(newlist))
    if i == 0:
        newlist.append(55)
    else:
        newlist = newlist + ['cantankerous']

    print(newlist, id(newlist))
# print('--- when using the accumulator, do not forget the bracket operator!')
# itemprint("newlist = newlist + 'wrong'", "print(newlist)")
# newlist += "wrong"
# print(newlist)
#
#
# # LISTS AND FOR LOOPS
# print('---LISTS AND FOR LOOPS---\n'
#       '--- the code above already iterates through a list by index\n'
#       '--- so the code below will only show traversing a list by item')
# itemprint("fruits = ['apple', 'cherry', 'banana']", "for afruit in fruit\n print(afruit):")
# fruits = ["apple", 'cherry', 'banana']
# for afruit in fruits:
#     print(afruit)
#
# print('--- since lists are mutable, it is often desirable to traverse a list,\n'
#       '--- modifying each of its elements as you go\n'
#       '--- the following code squares all the numbers 1 - 5 using iteration by position')
# itemprint("mylist = [1, 2, 3]", "for num in range(len(mylist): \n mylist[num] = mylist[num]**2", "print(mylist)")
# mylist = [1, 2, 3]
# for num in range(len(mylist)):
#     mylist[num] = mylist[num]**2
# print(mylist)
#
#
# # USING LISTS AS PARAMETERS
# def multlist(alist):
#     """
#     :param alist: a list of values to be doubled
#     :return: id of alist
#     """
#     for idx in range(len(alist)):
#         alist[idx] = alist[idx] * 2
#     return id(alist)
#
# mylist = [5, 10, 20]
# multlist(mylist)
# print(mylist)
# print("id mylist:", id(mylist), "id alist:", multlist(mylist))
#
# # Conclusion code should be for code
#







