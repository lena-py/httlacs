__author__ = 'lena'


def obj_test(vla, vlb):
    print("{} and {}".format(vla, vlb))
    test1 = str(vla is vlb)
    test2 = str(vla == vlb)
    test3 = str(id(vla) == id(vlb))
    print("a is b: {:^21} \na == b: {:^21} \nid(a) == id(b): {}\n".format(test1, test2, test3))

# String variables with same value reference same object
obj_test("help", "help")

# Lists with same values do not point to same object...
a = [1, 2, [4, 8], (5, 9)]
b = [1, 2, [4, 8], (5, 9)]
obj_test(a, b)

# ...but their elements do if they are immutable!
obj_test(a[0], b[0])
obj_test(a[2], b[2])
obj_test(a[3], b[3])

