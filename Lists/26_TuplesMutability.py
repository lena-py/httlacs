__author__ = 'lena'

# Create tuple
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[0:5])
print(id(julia))

# Modify tuple by slicing old tuple (creates new obj)
julia = julia[0:3] + ("Eat, Pray, Love", 2010) + julia[5:]
print(julia)
print(len(julia))
print(id(julia))

# Single element tuple
tup = (5,)
anint = 5
print(type(tup))
print(type(anint))

# Paren not necessary
tup = 5,
print(type(tup))
