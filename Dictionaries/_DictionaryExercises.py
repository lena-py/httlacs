__author__ = 'lena'
import string

# Exercise 1: Accept a string.  Return letters and no. of occurrences
a = "This Is a CommanD: abracadabR a."
a = a.lower()
b = ""
for i in a:
    if i in string.ascii_lowercase:
        b += i

letters = {}
for i in b:
    if i not in letters:
        letters[i] = b.count(i)

keys = list(letters.keys())
keys.sort()
for i in keys:
    print("{} {}".format(i, letters[i]))