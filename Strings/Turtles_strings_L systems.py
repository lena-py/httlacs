__author__ = 'lena'

# EXAMPLE 1


def apply_rules(lhchar, ax1, rul1, ax2="z", rul2="z"):
    """
    Takes a single character and applies the L-system rules to it
    Generalized to receive generic axioms and rules
    """
    # Rule 1
    if lhchar == ax1:
        rhstr = rul1
    # Rule 2
    elif lhchar == ax2:
        rhstr = rul2
    else:
        rhstr = lhchar

    return rhstr


def process_string(oldstring, a1, rul1, a2="z", rul2="z"):
    """
    Creates the L-system string for one transformation
    """
    newstr = ""
    for ch in oldstring:
        newstr = newstr + apply_rules(ch, a1, rul1, a2, rul2)

    return newstr


def create_L_system(iters, axiom, a1, rul1, a2="z", rul2="z"):
    """
    Creates the expanded L-system string, repeated (iters) times
    Doesn't use the accumulator because the string is entirely transformed
    """
    startstring = axiom
    endstring = ""
    for i in range(iters):
        endstring = process_string(startstring, a1, rul1, a2, rul2)
        startstring = endstring

    return endstring

print(create_L_system(4, "A", "A", "BAB"))


"----------------------------------------------------------------------------------------------------------------------"
# Example 2


def apply_rules2(lhch):
    rhstr = ""
    if lhch == "A":
        rhstr = "AB"
    elif lhch == "B":
        rhstr = "BAB"
    else:
        rhstr = lhch

    return rhstr


def process_string2(oldstr):
    newstr = ""
    for char in oldstr:
        newstr = newstr + apply_rules2(char)

    return newstr


def create_l_system2(axm, itrs):
    startstring = axm
    endstring = ""
    for i in range(itrs):
        endstring = process_string2(startstring)
        startstring = endstring

    return endstring


print(create_l_system2("A", 2))


'----------------------------------------------------------------------------------------------------------------------'
# Example 3

import turtle


def apply_rules3(lhch):
    """
    F = go forwards
    B = go backwards
    - = turn right
    + = turn left
    """
    rhstr = ""
    if lhch == "F":
        rhstr = "F-F++F-F"
    else:
        rhstr = lhch

    return rhstr


def process_string3(oldstr):
    newstr = ""
    for char in oldstr:
        newstr = newstr + apply_rules3(char)

    return newstr


def create_l_system3(axm, itrs):
    lstring = axm
    for i in range(itrs):
        lstring = process_string3(lstring)

    return lstring


def draw_l_system3(trtl, instrctns, angl, dstnc):
    for i in instrctns:
        if i == "F":
            trtl.forward(dstnc)
        elif i == "B":
            trtl.backward(dstnc)
        elif i == "-":
            trtl.right(angl)
        elif i == "+":
            trtl.left(angl)


def main():
    lstring = create_l_system3("F", 5)
    slim = turtle.Turtle()
    slim.speed(0)
    wn = turtle.Screen()

    draw_l_system3(slim, lstring, 60, 1)


    wn.exitonclick()

main()




