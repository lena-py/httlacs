__author__ = 'lena'


def double_stuff(alist):
    """
    :param alist: create new list by multiplying elements of alist by 2
    :return: the new list
    """
    newlist = []
    for avalue in alist:
        new_elem = 2 * avalue
        newlist.append(new_elem)
    return newlist

mylist = [5, 10, 20]
print(mylist, double_stuff(mylist))
# Only way to modify mylist is to assign it to the return of double_stuff
mylist = double_stuff(mylist)
print(mylist)
