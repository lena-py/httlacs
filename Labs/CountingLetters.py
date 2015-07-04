__author__ = 'lena'

# One way to count occurrences of a letter in a string
def counta(wrd, ltr):
    count = 0
    for l in wrd:
        if l == ltr:
            count += 1
    return count

print(counta('banana', 'a'))

# Another way to count occurrences
print('banana'.count('a'))

# Now using a dictionary
def countltrs(word):
    dic = {}
    for l in word:
        dic[l] = word.count(l)
    return dic

ans = countltrs('banana')
print(ans.get('a', 0))
