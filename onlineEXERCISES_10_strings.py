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

# def find(astring, achar):
#     idx = 0
#     found = ""
#     while idx < len(astring):
#         if astring[idx] == achar:
#             found += "found at index " + str(idx) + "\n"
#         idx += 1
#     if found != "":
#         return found
#     else:
#         return -1
#
# mystring = input("enter a string\n")
# mychar = input("enter a character\n")
#
# print(find(mystring, mychar))


"""
To find the locations of the second or third occurrence of a character in a string,
we can modify the find function,
adding a third parameter for the starting position in the search string:
"""

#
# def find(astring, achar, start=0):
#     idx = start
#     found = ""
#     while idx < len(astring):
#         if astring[idx] == achar:
#             found += "found at index " + str(idx) + "\n"
#         idx += 1
#     if found != "":
#         return found
#     else:
#         return -1
#
# mystring = input("enter a string\n")
# mychar = input("enter a character\n")
# mystart = int(input("enter a starting position\n"))
#
# print(find(mystring, mychar, mystart))


"""
Adding another optional parameter to find
makes it search from a starting position,
up to but not including the end position.
"""


# def find(astring, achar, start=0, end=""):
#     idx = start
#     found = ""
#     if end == "":
#         end = len(astring)
#     else:
#         end = int(end)
#     while idx < end:
#         if astring[idx] == achar:
#             found += "found at index " + str(idx) + "\n"
#         idx += 1
#     if found != "":
#         return found
#     else:
#         return -1
#
# mystring = input("enter a string\n")
# mychar = input("enter a character\n")
# mystart = int(input("enter a starting position\n"))
# myend = input("enter a stop position\n")
#
# print(find(mystring, mychar, mystart, myend))


""" EXERCISES """
"""
In Robert McCloskey’s book Make Way for Ducklings,
the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.
This loop tries to output these names in order.
Of course, that’s not quite right because Ouack and Quack are misspelled. Can you fix it?
"""

# prefixes = "JKLMNOPQ"
# suffix = "ack"
#
# for p in prefixes:
#     if p == "O" or p == "Q":
#         print(p + "u" + suffix)
#     else:
#         print(p + suffix)


"""
Assign to a variable in your program
a triple-quoted string that contains your favorite paragraph of text
- perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.

Write a function
that counts the number of alphabetic characters
(a through z, or A through Z) in your text
and then keeps track of how many are the letter ‘e’.

Your function should print an analysis of the text like this:
Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.
"""

# import string
# total_count = 0
# found = 0
# para = """Where is it I've read that someone condemned to death says or thinks,
# an hour before his death, that if he had to live on some high rock,
# on such a narrow ledge that he'd only room to stand, and the ocean, everlasting darkness,
# everlasting solitude, everlasting tempest around him,
# if he had to remain standing on a square yard of space all his life, a thousand years, eternity,
# it were better to live so than to die at once. Only to live, to live and live! Life, whatever it may be!”
# """
#
# for char in para:
#     if char not in string.whitespace and char in string.ascii_letters:
#         if char == "e":
#             found += 1
#         total_count += 1
#
# percent = (found / total_count)
#
# print("Your text contains", total_count, "alphabetic characters, of which",
#       found, "({:.1%})".format(percent), "are 'e'")


"""
Print out a neatly formatted multiplication table, up to 12 x 12.
"""
mult = 1

while mult < 13:
    for i in range(1, 13):
        print(i*mult, "\t", end=" ")
    mult += 1
    print("\n")



