__author__ = 'lena'

mylist = [1, 2, 4, 5]
newlist = [item * 2 for item in mylist if item > 2]
print(newlist)

wordlist = ["apple", "banana", "grapes", "mango"]
newlist = [fruit for fruit in wordlist if "e" in fruit]
print(newlist)

numlist = [5, 10, 12, 18, 28, 33]
newlist = [num // 2 for num in numlist if num % 2 == 0]
print(newlist)
