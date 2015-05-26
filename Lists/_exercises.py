__author__ = 'lena'

ex = "Exercise 01"
print(ex)
# Demonstrate how to clone a list, and that the new list is not an alias
firstlist = [1, 2, 3]
secondlist = firstlist[:]
secondlist[0] = 5

for alist in (firstlist, secondlist):
    print(alist, id(alist))


ex = "Exercise 02"
print(ex)
# Create a list called firstlist with the following six items: 76, 92.3, “hello”, True, 4, 76.
# Do it with both append and with concatenation, one item at a time.
firstlist = []
firstlist.append(76)
firstlist = firstlist + [92.3]
firstlist.append("hello")
firstlist = firstlist + [True]
firstlist.append(4)
firstlist = firstlist + [76]
print(firstlist)


ex = "Exercise 03"
print(ex)
# Starting with the list in Exercise 2, write Python statements to do the following:
# Append “apple” and 76 to the list.
for item in ("apple", 76):
    firstlist.append(item)
print(firstlist)

# Insert the value “cat” at position 3.
firstlist.insert(3, "cat")
print(firstlist)

# Insert the value 99 at the start of the list.
firstlist.insert(0, 99)
print(firstlist)

# Find the index of “hello”.
print(firstlist.index("hello"))

# Count the number of 76s in the list.
print(firstlist.count(76))

# Remove the first occurrence of 76 from the list.
firstlist.remove(76)
print(firstlist)

# Remove True from the list using pop and index.
firstlist.pop(-5)
print(firstlist)


ex = "Exercise 04"
print(ex)
# Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module).
# Write a function called average that will take the list as a parameter and return the average.
import random


def average(anylist):
    numerator = 0
    denominator = len(anylist)
    for num in range(len(anylist)):
        numerator += anylist[num]
    return [numerator, denominator, numerator / denominator]


def createlist():
    mylist = []
    for i in range(100):
        i = random.randint(0, 1001)
        mylist.append(i)
    return mylist

currentlist = createlist()
nmrtr = average(currentlist)[0]
dnmntr = average(currentlist)[1]
avg = average(currentlist)[2]

print("numerator:", nmrtr, "denominator:", dnmntr, "average:", avg)


ex = "Exercise 05"
print(ex)
# Write a Python function that will take a list of 100 random integers between 0 and 1000
# and return the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)


def find_max(anylist):
    x = 0
    for i in range(len(anylist)):
        y = anylist[i]
        if y > x:
            x = y
    return x

currentlist = createlist()
print(find_max(currentlist))


ex = "Exercise 06"
print(ex)
# Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs.
# For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:


def sum_of_sqaures(xs):
    newlist = [numbr ** 2 for numbr in xs]
    answer = 0
    for i in newlist:
        answer += i
    return answer

currentlist = [2, 3, 4]
print(sum_of_sqaures(currentlist))


ex = "Exercise 07"
print(ex)
# Write a function to count how many odd numbers are in a list.


def odd_numbers(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            count += 1
    return count

currentlist = [1, 3, 9, 2, 4, 8]
print(odd_numbers(currentlist))


ex = "Exercise 08"
print(ex)
# Sum up all the even numbers in a list.


def sum_evens(lst):
    answer = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            answer += lst[i]
    return answer

currentlist = [1, 2, 3, 4, 5, 6]
print(sum_evens(currentlist))


ex = "Exercise 09"
print(ex)
# Sum up all the even numbers in a list.


def sum_odds(lst):
    answer = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            answer += lst[i]
    return answer

print(sum_odds(currentlist))


ex = "Exercise 10"
print(ex)
# Sum up all the negative numbers in a list.


def sum_negs(lst):
    answer = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            answer += lst[i]
    return answer

currentlist = currentlist + [-1] + [-2]
print(sum_negs(currentlist))


ex = "Exercise 11"
print(ex)
# Count how many words in a list have length 5.


def countfives(lst):
    answer = 0
    for i in range(len(lst)):
        if len(lst[i]) == 5:
            answer += 1
    return answer

currentlist = ["hello", "world", "might", "return", "blanket", "paris", "michael", "peace"]
print(countfives(currentlist))


ex = "Exercise 12"
print(ex)
# Sum all the elements in a list up to but not including the first even number.


def sum_some(lst):
    answer = 0
    i = 0
    while lst[i] % 2 != 0:
        answer += lst[i]
        i += 1
    return answer

currentlist = [1, 3, 5, 1, 2, 5, 2]
print(sum_some(currentlist))


ex = "Exercise 13"
print(ex)
# Count how many words occur in a list up to and including the first occurrence of the word “sam”


def count_words(lst):
    i = 0
    while lst[i] != "sam":
        i += 1
    return i

currentlist = ["orange", "cat food", "sam", "likewise"]
print(count_words(currentlist))


ex = "Exercise 14"
print(ex)
# Implement a Python function that works like the following: count, in, reverse, index, insert


def count_items(lst, itm):
    answer = 0
    for i in range(len(lst)):
        if lst[i] == itm:
            answer += 1
    return answer


def list_in_function(lst, itm):
    answer = 0
    for i in range(len(lst)):
        if lst[i] == itm:
            answer += 1
    if answer > 0:
        return True
    else:
        return False


def reverse_list(lst):
    answer = []
    for i in range(len(lst), 0, -1):
        answer.append(lst[i - 1])
    return answer

currentlist = [1, 2, 5, 7, 1, 5, 9, 8]

print("count:", currentlist.count(1))
print("count:", count_items(currentlist, 1))

print("in:", 1 in currentlist)
print("in:", list_in_function(currentlist, 1))

newlist = currentlist[:]
newlist.reverse()
print("reverse:", newlist)
print("reverse:", reverse_list(currentlist))

