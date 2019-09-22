'''Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa?”'''


'''def uses_only(word, letters):
   
    for letter in word:
        if letter not in letters:
            return False
    return True
#print(uses_only("hello","4"))'''

myfile = open("words.txt")

def uses_only(word, string):
    for char in word:
        if char not in string:
            return False
    return True

def word_find():
    count = 0
    enter_string = input("enter the letters:")
    for line in myfile:
        word = line.strip()
        if uses_only(word, enter_string):
            print (word)
            count += 1
    print (count)

word_find()