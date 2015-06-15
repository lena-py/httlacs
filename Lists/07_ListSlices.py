__author__ = 'lena'

# Slice operator works on lists
list1 = [1, 2, 3, 4, 5, 6]
hf_list = len(list1)//2
f_half = list1[:hf_list]
s_half = list1[hf_list:]
print("The first half of the list is {} and the second half is {}".format(f_half, s_half))