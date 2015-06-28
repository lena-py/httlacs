__author__ = 'lena'

# Modify a list in a function
def mod_list(lst):
    """
    Modify each elem in a list with double its value
    :param lst: orig list
    :return: mod list and param id
    """
    for i in range(len(lst)):
        lst[i] *= 2
    lstid = id(lst)
    return lst, lstid

mylist = [1, 3, 5]
print(mod_list(mylist)[0])

# The param lst and the var/arg mylist are aliases for the same obj
print(id(mylist))
print(mod_list(mylist)[1])