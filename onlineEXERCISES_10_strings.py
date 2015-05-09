# slice operator

# singers = "Peter, Paul, and Mary"
# print(singers[0:5])
# print(singers[7:11])
# print(singers[17:21])

# ordinal values

# import string as str
#
# for i in str.printable:
#     print("The ordinal number of", i, "is", ord(i))

# convert string to lowercase and integer to ordinal number

# word = "SAMMY TAYLOR"
# print(word.lower())
# print(word)
#
# for i in range(100000):
#     print(i, "converts to", chr(i))
#
# print(chr(188))

# strings are immutable

# word = "Hello"
# s = "J" + word[1:]
# print(s)

# traversal and the for loop

# by item
# for char in "test and test":
#     print(char)

# by index
# fruit = "apple"
# for idx in range(len(fruit)):
#     print(fruit[idx])


# by index, backwards
# fruit = "apple"
# for idx in range(len(fruit)-1, -1, -1):  # start at 1 minus the length, upper bound is -1, step -1
#     print(fruit[idx])

# traversal and the while loop

# fruit = "apple"
# counter = 0
#
# while counter < len(fruit):
#     print(fruit[counter])
#     counter += 1

# THE ACCUMULATOR PATTERN WITH STRINGS
# Combining the in operator with string concatenation using + and the accumulator pattern,
# we can write a function that removes all the vowels from a string.
# The idea is to start with a string and iterate over each character,
# checking to see if the character is a vowel. As we process the characters,
# we will build up a new string consisting of only the nonvowel characters.
# To do this, we use the accumulator pattern.

# import string
# a = "mississIppi"
# vowels = "aeiouAEIOU"
# z = ""
# print(string.ascii_letters)
# for char in a:
#     if char not in vowels:
#         z += char
#     else:
#         print("no")
#
# print(z)

# Turtles and Strings and L-Systems
# unattempted


"""
# The following program counts
# the number of times a particular letter, lttr,
# appears in a string.
"""


# def count_char(s, lttr):
#     found = 0
#     for achar in s:
#         if achar == lttr:
#             found += 1
#     return found
#
#
# def main():
#     strng = input("enter a string\n")
#     lttr = input("enter a letter\n")
#     print(count_char(strng, lttr))
#
#
# if __name__ == "__main__":
#     main()


"""
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
"""


def find(astring, achar):
    idx = 0
    found = ""
    while idx < len(astring):
        if astring[idx] == achar:
            found += "found at index " + str(idx) + "\n"
        idx += 1
    if found != "":
        return found
    else:
        return -1

mystring = input("enter a string\n")
mychar = input("enter a character\n")

print(find(mystring, mychar))


"""
To find the locations of the second or third occurrence of a character in a string,
we can modify the find function,
adding a third parameter for the starting position in the search string:
"""


def find(astring, achar):
    idx = 0
    found = ""
    while idx < len(astring):
        if astring[idx] == achar:
            found += "found at index " + str(idx) + "\n"
        idx += 1
    if found != "":
        return found
    else:
        return -1

mystring = input("enter a string\n")
mychar = input("enter a character\n")

print(find(mystring, mychar))




