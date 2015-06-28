__author__ = 'lena'

# Extract the nested list and then the elem...
nested = ["hello", 1, 2, [10, 20]]
innerlist = nested[3]
item = innerlist[1]
print(item)

# ... Or use successive bracket operators to access item directly
item = nested[3][1]
print(item)

# Example 2
alist = [[4, [True, False], 6, 8], [888, 999]]
if alist[0][1][0]:
    print(alist[0][1][0])

# Example 3
anotherlist = [1*2, 52, 1, 98]
mylist = [elem for elem in anotherlist if elem > 1]
print(mylist)
