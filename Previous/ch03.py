__author__ = 'lena'

# write a function called nine_lines that uses three_lines to print nine blank lines
# then add a function named clear_screen that prints out 25 blank lines
# the last line of the program should be a call to clear_screen


def three_lines():
    print()
    print()
    print()


def nine_lines():
    three_lines()
    three_lines()
    three_lines()


# clear_screen() satisfies last criterion for exercise
def clear_screen():
    nine_lines()
    nine_lines()
    nine_lines()

# Fill in the body of the function definition for cat_n_times
# so that it will print the string s, n times


def cat_n_times(s, n):
    print(s * n)


