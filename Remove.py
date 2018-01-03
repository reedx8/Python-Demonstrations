'''Codewars: Remove First and Last Character'''
# Remove.py: goal is to create a function that removes the first and last characters of a string (string = a single word, not a sentence apparently)
# It took me maybe little less than a week to figure this out, but my breakthrough came when i realized explicitly that strings are immutable, so i decided to try and convert them to a list. i had tried the augmented assignment operator -= but it does not work on strings i found out.

def remove_char(string):
    listString = list(string)
    del listString[0]; del listString[-1]
    joined = ''.join(listString)
    print(joined)

word = input("Give me a word: ")
remove_char(word)
