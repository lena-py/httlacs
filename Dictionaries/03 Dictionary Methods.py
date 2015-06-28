__author__ = 'lena'

chunks_dict = {'directory': "06 01 00 00, 08 01 00 00, 0c 00 00 0c", 'chunks': "chunk data"}
animal_dict = {'cat': 12, 'dog': 14, 'elephant': 120, 'bear': 30}

# Keys method
kyslst = chunks_dict.keys()
print("kyslst is:", kyslst)

# Create list from keys method
ks = list(kyslst)
print("kyslst as an actual list", ks, "\n")

# Use sort list method
alist = list(animal_dict.keys())
alist.sort()
print(alist)

# Iterate over keys
for akey in kyslst:
    print("Got key {} which maps to value {}".format(akey, chunks_dict[akey]))
for akey in chunks_dict:     # Stated more simply than above
    print("same as above")
if "directory" in chunks_dict:
    print("the file has a directory")

# Values method returns all values in the dict
valus = chunks_dict.values()
vls = list(valus)
print(valus)
print(vls)

# Items method returns keys and values as a list of tuples
itms = chunks_dict.items()
lstitms = list(itms)
print(itms)
print(lstitms)

# Iterate over items
for (k, v) in itms:
    print("{} goes with {}".format(k, v))

# Get method returns value for key
get = chunks_dict.get('chunks', 'nothing with that key')
print(get)
get_key_alt = chunks_dict.get('chunls', 'nothing with that key')
print("get_key_alt is", get_key_alt)