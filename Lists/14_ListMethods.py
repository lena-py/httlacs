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