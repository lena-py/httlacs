__author__ = 'lena'

# Append modifies original list
newlist = [1, 3, 5]
print(id(newlist))
newlist.append(12)
print(id(newlist))

# Assignment operator with concantenation operator creates new object
newlist = newlist + [12]
print(id(newlist))

# Bracket operator must be used with the accumulator
newlist += ["wrong"]
newlist += "wrong"
print(newlist)