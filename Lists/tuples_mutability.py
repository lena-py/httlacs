__author__ = 'lena'

# Create tuple
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[0:5])

# Modify tuple by slicing old tuple
julia = julia[0:3] + ("Eat, Pray, Love", 2010) + julia[5:]
print(julia)
print(len(julia))

# Single element tuple
tup = (5,)
print(type(tup))
