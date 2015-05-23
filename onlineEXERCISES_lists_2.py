__author__ = 'lena'


def itemprint(a="", b="", c="", d="", e="", f=""):
    for i in (a, b, c, d, e, f):
        if i != "":
            print(">>>", i)


# LIST METHODS
print('---LIST METHODS---\n'
      '--- use the append method to add elements to the end of a list')
itemprint("newlist = list()", "newlist.append(5)", "print(newlist)")
newlist = list()
newlist.append(5)
print(newlist)
itemprint("newlist.append(10)", "print(newlist)")
newlist.append(10)
print(newlist)

print('--- use the insert method to add an elements at a specified index (idx, vlu)')
itemprint("print(newlist.insert(1, 12))", "print(newlist")
newlist.insert(1, 12)
print(newlist)

print('--- use the count method to determine the number of occurrences of a value in the list')
itemprint("print(newlist.count(12))")
print(newlist.count(12))

print('--- use the index method to get the index of the first occurrences of the value')
itemprint("print(newlist.index(10)")
print(newlist.index(10))

print('--- use the reverse method to ummm...reverse the list elements')
itemprint("newlist.reverse()", "print(newlist)")
newlist.reverse()
print(newlist)

print('--- use the sort method to rearrange the list elements\n'
      '--- cannot sort int and str')
itemprint("newlist.sort()", "print(newlist)")
newlist.sort()
print(newlist)

print('--- use the remove method to remove the first occurrence of a value')
itemprint("newlist.remove(5)", "print(newlist)")
newlist.remove(5)
print(newlist)

print('--- use the pop method to remove and return item at specified idx (default last)')
itemprint("lastitem = newlist.pop()", "print(lastitem)")
lastitem = newlist.pop()
print(lastitem)
itemprint("print(newlist)")
print(newlist)


# APPEND VS. CONCATENATE
print('---APPEND VS. CONCATENATE---\n'
      '--- use append to add an item to the end of a list\n'
      '--- use accumulator operation to create a new list and append the item')
example = ["newlist.append(55)", "newlist = newlist + ['cantankerous']"]
for i in range(len(example)):
    itemprint("print(id(newlist))")
    print(id(newlist))
    itemprint(example[i])
    if i == 0:
        newlist.append(55)
    else:
        newlist = newlist + ['cantankerous']
    itemprint("print(newlist), id(newlist))")
    print(newlist, id(newlist))
print('--- when using the accumulator, do not forget the bracket operator!')
itemprint("newlist = newlist + 'wrong'", "print(newlist)")
newlist += "wrong"
print(newlist)


# LISTS AND FOR LOOPS
print('---LISTS AND FOR LOOPS---\n'
      '--- the code above already iterates through a list by index\n'
      '--- so the code below will only show traversing a list by item')
itemprint("fruits = ['apple', 'cherry', 'banana']", "for afruit in fruit\n print(afruit):")
fruits = ["apple", 'cherry', 'banana']
for afruit in fruits:
    print(afruit)

print('--- since lists are mutable, it is often desirable to traverse a list,\n'
      '--- modifying each of its elements as you go\n'
      '--- the following code squares all the numbers 1 - 5 using iteration by position')
itemprint("mylist = [1, 2, 3]", "for num in range(len(mylist): \n print(num**2)")
mylist = [1, 2, 3]
for num in range(len(mylist)):
    mylist[num] = mylist[num]**2
print(mylist)

the




