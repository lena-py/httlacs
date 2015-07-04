__author__ = 'lena'

# Aliasing exists for dicts...
opposites = {'hot': 'cold', 'left': 'right', 'up': 'down', 'in': 'out'}
alias = opposites
print(alias is opposites)
print("dict1 id {}\ndict2 id {}".format(id(opposites), id(alias)))

# ... so modifying dict affects both obj
opposites['hate'] = 'love'
print(list(alias.keys()))
print(list(opposites.keys()))

# Copy a list to modify it but keep the original
acopy = opposites.copy()
print(id(acopy))

# Modifying the copy does not change the original
acopy['soft'] = 'hard'
print('soft' in opposites)
print('soft' in acopy)