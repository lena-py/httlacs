# LIST VALUES
"""
we can also assign list values to variables and pass lists as parameters to functions.
"""
import math
import inspect

def power(y):
    return math.pow(10, y)

mixed_list = ["hello world", 10*2, [10, 2]]
a = [10, 20, 30, [30, 40]]
new_list = [mixed_list, a]
# print(power(a[0]))
# print(mixed_list)
# print(new_list)

print('---LIST LENGTH---')
print(len(mixed_list))
print(len(a))
print(len(new_list))
# prints the uppercase of the first list item, but only the first 5 characters
print(mixed_list[0].upper()[0:1+4])


print('---LIST MEMBERSHIP---')
print("hello world" in mixed_list)
print("hello" in mixed_list)
print("hello" not in mixed_list)
print(40 in a)
print(2 in mixed_list)


print('---ACCESSING ELEMENTS---\n'
      'use index operator')
numbers = [4, 'cat', 376, 2*10, 0, -12, len('sgt')]
print(numbers[2])
print(numbers[9-8])
print(numbers[-2])
print(numbers[len(numbers)-1])

print('successive indices')
print(numbers[1].upper()[0] + numbers[1][1:])


def concat_example(ex1="", ex2="", ex3="", ex4=""):
    newx = []
    stringprint = ""
    for i in [ex1, ex2, ex3, ex4]:
        if type(i) != str:
            newx += i
            stringprint += str(i)
            print(type(newx))
    print("concatenating", stringprint, "becomes...\n>>>", newx, "\n-----")


print('---CONACATENATION AND REPETITION---')
fruit = ['apples', 'bananas', 'guanabanas', 'pears', 'candy']
print(fruit + [6, 7, 8, 9])
concat_example([1, 2], [3, 4])
concat_example((fruit, [6, 7, 8, 9]))
# concat_example("[0] * 4", [1], 4)

print([0] * 4)
print([1, 2, ['hello', 'goodbye']] * 2)

""" id is the unique identifier for objects corresponding to an address in memory"""
print(id(fruit))


# LISTS ARE MUTABLE
print('---LISTS ARE MUTABLE---')
print('---use the slice operator on the left side of an expression to modify an item in a list')


def fruitlist(lst):
    return print("fruits are:", lst[:])

fruit = ["banana", "apple", "cherry"]
fruitlist(fruit)
print(">>> fruit[0] = 'orange'")
fruit[0] = 'orange'
fruitlist(fruit)
print(">>> fruit[-1] = 'pear'")
fruit[-1] = 'pear'
fruitlist(fruit)

print('---combine item assignment with slice operator to update several elements at once')
print(">>> fruit[0:2] = ['apricot', 'lemon]")
fruit[0:2] = ['apricot', 'lemon']
fruitlist(fruit)

print('---remove elements by assigning the empty list to them')
print(">>> fruit[-1:-2] = []")
fruit[-1:-2] = []
fruitlist(fruit)

print('---insert elements into a list by squeezing them into an empty slice at the desired location')
print(">>> fruit [1:1] = ['kiwi', 'guava'")
fruit[1:1] = ['kiwi', 'guava']
fruitlist(fruit)


# LIST DELETION
print('---LIST DELETION---')
print('---use the del statement to remove items from lists (not the slice/empty list idea above)')
fruitlist(fruit)
print(">>> del fruit[0:2]")
del fruit[0:2]
fruitlist(fruit)
print(">>> del fruit[-1]")
del fruit[-1]
fruitlist(fruit)


# OBJECTS AND REFERENCES
print('---OBJECTS AND REFERENCES---\n'
      '---immutable data types (str, int) with the same value refer to the same object\n'
      '---this relationship does not extend to mutable data types (lists).  even though a == b, a is not b\n'
      '---one exception to above is if you assign the b = a, '
      'then this results in the same objects referenced by both var, even mutables (ALIASING!)\n'
      '---the code below uses an interesting loop.  to get around b = a issue I used b = a[:] (CLONING!)')


def print_format(x, y):
    return print(">>> a = {0}\n".format(x) +
                 ">>> b = {0}".format(y))


def ref_same_object(x, y):
    print_format(x, y)
    print(">>> a is b")
    return print(x is y)


def same_value(x, y):
    print(">>> a == b")
    return print(x == y)


def show_id(x, y):
    print(">>> id(a), id(b)")
    return print(id(x), id(y))


def listid(x=None, y=None):
    i = 0
    if x is not None:
        while i < len(x):
            print(">>> id(a[{0}]): ".format(i) + str(id(x[i])))
            i += 1

    else:
        while i < len(y):
            print(">>> id(b[{0}]): ".format(i) + str(id(y[i])))
            i += 1


for a in ("'banana'", [1, 2, 3]):
    # just b = a results in the same object for both immutable and mutable data types, using the slice operator extracts
    # the values I guess...it just came to me that it might work
    b = a[:]
    ref_same_object(a, b)
    same_value(a, b)
    show_id(a, b)

print('---\n---a list is a collection of references to objects.  a variable assigned to a list is a reference to '
      'a collection of references')
print(">>> b =", b)
print(">>> id(b):", id(b))
listid(None, b)


# ALIASING
print("---ALIASING---\n"
      "---as shown above, assigning one variable to another points it to the same object.  This is aliasing\n"
      "---changes made to one variable of an aliased object affect the other\n"
      "---best practice is to avoid aliasing mutable objects")
print(">>> a = b")
a = b
ref_same_object(a, b)
same_value(a, b)
show_id(a, b)
print(">>> a[0] = 5")
a[0] = 5
print(">>> print b")
print(b)


# CLONING
print("---CLONING---\n"
      "---pretty sweet that I figured this out on my own, too.\n"
      "---b = a[:] clones a and creates a second object that it not influenced by changing the first object"
      "---this is despite the list elements' id's being the same.")
print(">>> b = a[:]")
b = a[:]
ref_same_object(a, b)
same_value(a, b)
show_id(a, b)
listid(a, None)
listid(None, b)
print("huh. check it out. id of a[0]", id(a[0]), "id of b[0]", id(b[0]))
print("now change b[0] to 10 and reprint a[0] and id and b[0]'s id")
b[0] = 10
print(a[0], id(a[0]), id(b[0]))


# REPETITION AND REFERENCES
print("---REPETITION AND REFERENCES---\n"
      "---using the repetition operator on a variable that is a list creates additional elements\n"
      "that reference the same objects\n"
      "---using the repetition operator on a list variable with the bracket operator creates aliases, not clones\n"
      "---modifying the original list, or a subelement of the new list, changes all the values")
print(">>> newlist = a * 3")
newlist = a * 3
print(newlist)
listid(newlist)
print(">>>newlist[0] = 1")
newlist[0] = 1
print(newlist)
print(">>> newlist = [a] * 3")
newlist = [a] * 3
print(newlist)
listid(newlist)
print(">>> newlist[0][0] = 12")
newlist[0][0] = 12
print(newlist)
print(">>> a[0] = 0")
a[0] = 0
print(">>> print(newlist)")
print(newlist)












