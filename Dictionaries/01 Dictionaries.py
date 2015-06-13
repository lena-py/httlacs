__author__ = 'lena'

# First method of creating a dictionary
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

# Second method of creating a dictionary
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'quatro'}

# Accessing list items
print(eng2sp['two'])

# Using variables to create dictionaries
eng2sp = {}
sp_nums = ["", "uno", "dos", "tres", "quatros", "cinqo", "six", "ciete", "ocho", "nueve", "deis"]
for i in range(1, 11):
    eng2sp[i] = sp_nums[i]

print(eng2sp)
