__author__ = 'lena'

# List traversal by item
newlist = ["cherry", "banana", "apple", "orange", "grapefruit"]
for afruit in newlist:
    print(afruit)

# List traversal by index
for position in range(len(newlist)):
    print(newlist[position])

# Modify list elements with traversal
newlist = [1, 3, 5]
for i in range(len(newlist)):
    newlist[i] **= 2
print(newlist)