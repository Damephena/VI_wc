# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'

def new_word(word):
    if len(word) > 4:
        print(word[:2] + word[-2:])
    else:
        print ("Word cannot form expected result: " + word)

word = str(input('enter a word or sentence: '))
new_word("This is me in 3D")

# Write a Python program to calculate the length of a string
def string_length(strings):
    print("This string has: ", len(strings), " characters")
word = str(input('enter a string: '))
string_length(word)

# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def single_string(firstWord, nextWord):
    first_swap = nextWord[:2] + firstWord[2:]
    second_swap = firstWord[:2] + nextWord[2:]
    print(first_swap, '', second_swap)

a = str(input('enter a word: '))
b = str(input('enter another word: '))
single_string(a, b)

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def verb(str):
    if len(str) > 3:
        if str[-3:] == 'ing':
            print(str + 'ly')
        else:
            print(str + 'ing')
    else:
        print(str)

word = str(input('enter a word: '))
verb("ing")
