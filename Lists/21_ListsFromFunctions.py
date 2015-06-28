__author__ = 'lena'
import random


def rndmint():
    return random.randint(0, 100)


def rndm_lst(elems):
    newlist = []
    for i in range(elems):
        x = rndmint()
        newlist.append(x)
    return newlist

print(rndm_lst(5))

