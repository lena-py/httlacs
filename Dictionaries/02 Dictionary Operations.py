__author__ = 'lena'

fruit = {'apples': 430, 'pears': 12, 'strawberries': 124}

# Someone buys all the pears:
del fruit['pears']

# Add the pears back:
fruit['pears'] = 12

# Leave the pears in the inventory, but reduce count by a number
fruit['pears'] -= 1

# Add 200 more pears to the inventory
fruit['pears'] += 200

print(fruit)
print(len(fruit))

'-----------------------------------------------------------------'

# Create a dictionary, add two values together to create a new item

mydict = {'cat': 12, 'dog': 15}
mydict['mouse'] = mydict['cat'] + mydict['dog']
print(mydict)

