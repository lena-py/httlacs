__author__ = 'lena'

# Use existing knowledge to sum a list of numbers
alist = [1, 3, 5, 7, 9]

total = 0
for i in alist:
    total += i

print(total)


# Sum the list without a for or while loop
def sum_list(number_list):
    if len(number_list) == 1:
        return number_list[0]
    else:
        return number_list[0] + sum_list(number_list[1:])

print(sum_list(alist))