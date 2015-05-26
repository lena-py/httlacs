__author__ = 'lena'
import random


def randomint():
    return random.randint(0, 100)


def list_from_random(elems):
    newlist = []
    for i in range(elems):
        x = randomint()
        newlist.append(x)
    return newlist

print(list_from_random(5))

