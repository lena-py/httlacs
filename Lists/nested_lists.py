__author__ = 'lena'

# Example 1
nested = ["hello", 1, 2, [10, 20]]
innerlist = nested[3]
item = innerlist[1]

print(item)
# Use successive bracket operators to access item directly
item = nested[3][1]

print(item)


# Example 2
alist = [[4, [True, False], 6, 8], [888, 999]]
if alist[0][1][0]:
    print(True)


# Example 3
anotherlist = [1*2, [1, 3], 1, 98]
mylist = [elem for elem in anotherlist]
print(mylist)
