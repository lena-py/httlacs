__author__ = 'lena'

# wrap the code in a function
# call it three times to demonstrate the function


def compare(x, y):
    if x < y:
        print(x, "is less than", y)
    elif x > y:
        print(x, "is greater than", y)
    else:
        print(x, "and", y, "are equal")

'-----------------------------------------------------------'

# truth tables
# create a truth table to learn about boolean expressions


def truth_table(expression):
    header = (" p      q      %s" % expression)
    print(header)
    print("=" * len(header))

    for p in True, False:
        for q in True, False:
            print("%-7s %-7s %-7s" % (p, q, eval(expression)))

