__author__ = 'lena'


def convert_number(number):
    if len(str(number)) == 1:
        return str(number)
    else:
        return str(number[0]) + convert_number(number[1:])

print(convert_number(745))