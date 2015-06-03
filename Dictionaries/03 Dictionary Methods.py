__author__ = 'lena'

chunks_dict = {'directory': "06 01 00 00, 08 01 00 00, 0c 00 00 0c", 'chunks': "chunk data"}

# Keys method
keys_list = chunks_dict.keys()
print("keys_list is:", keys_list)
ks = list(keys_list)
print("keys_list as an actual list", ks, "\n")


for akey in keys_list:
    print("Got key", akey, "which maps to value", chunks_dict[akey])
for akey in chunks_dict:     # Stated more simply than above
    print("Aloha")
print("ß")



# Values method
keys_values = chunks_dict.values()
print("keys_values are:", keys_values)

keys_items = chunks_dict.items()
print("keys_items are:", keys_items)
print(type(keys_items))

get_key = chunks_dict.get('chunks')
print("get_key for 'chunks' is:", get_key)

get_key_alt = chunks_dict.get('chunls', 'chunks')
print("get_key_alt is", get_key_alt)


