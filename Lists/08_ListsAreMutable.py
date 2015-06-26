__author__ = 'lena'

# Item assignment
list1 = [[b'0100', b'0100', b'4300', b'4300', b'4400', b'0100'], [b'0100', b'4300']]
list1[1][0] = b'0200'
print(list1)

# Multiple item assignment (note line 10 overwrites three elements with two elements)
list1[1][:] = b'0300', b'0100'
list1[0][:3] = list1[1]
print(list1)

# Remove elements
list1[0][1:3] = []
print(list1)

# Insert elements
list1[1][0:0] = ["insert", "another"]
print(list1)