__author__ = 'lena'
import string

# Exercise 1: Accept a string.  Return letters and no. of occurrences
a = "This Is a CommanD: abracadabR a."
a = a.lower()
b = ""
for i in a:
    if i in string.ascii_lowercase:
        b += i

letters = {}
for i in b:
    if i not in letters:
        letters[i] = b.count(i)

keys = list(letters.keys())
keys.sort()
for i in keys:
    print("{} {}".format(i, letters[i]))


# Exercise 2: Various dictionary methods
def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    import sys

    linenum = sys._getframe(1).f_lineno  # get the caller's line number.
    if expected == actual:
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
               .format(linenum, expected, actual))
    print(msg)


def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    pass

# make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
test('strawberries' in new_inventory, True)
test(new_inventory['strawberries'], 10)
add_fruit(new_inventory, 'strawberries', 25)
test(new_inventory['strawberries'], 35)


# Exercise 3: Write a file that counts Alice in Wonderland words
f = open('AIW.rtf', 'r')

count = {}

for line in f:
    for word in line.split():
        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore case
        word = word.lower()

        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

keys = list(count.keys())
keys.sort()

# save the word count analysis to a file
out = open('alice_words.txt', 'w')

for word in keys:
    out.write(word + " " + str(count[word]))
    out.write('\n')

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")


# Exercise 4: What is the longest word in AiW?
longest_word = ""
for akey in keys:
    if len(akey) > len(longest_word):
        longest_word = akey
print("The longest word is {} with {} characters".format(longest_word, len(longest_word)))


# Exercise 5: English to Pirate translator
english = ["sir", "hotel", "student", "boy", "madam", "professor", "restaurant", "your",
           "excuse", "students", "are", "lawyer", "the", "restroom", "my", "hello", "is", "man"]

pirate = ["matey", "fleabag inn", "swabbie", "matey", "proud beauty", "foul blaggart", "galley", "yer",
          "arr", "swabbies", "be", "foul blaggart", "th", "head", "me", "avast", "be", "matey"]

translator = {}


for e, p in zip(english, pirate):
    translator[e] = p

sentence = input("Enter a sentence in English\n")
pirate_sentence = ""
words = sentence.split()
for aword in words:
    if aword in translator:
        pirate_sentence += translator[aword] + " "
    else:
        pirate_sentence += aword + " "

print(pirate_sentence)