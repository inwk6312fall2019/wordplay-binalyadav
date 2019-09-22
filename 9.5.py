'''Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?'''




def uses_all(word, string):
    for char in string:
        if char not in word:
            return False
    return True

wordlist = open("words.txt")

def find_word():
    count = 0
    enter_letter = input("Enter letter")
    enter_letter = enter_letter.lower()

    for line in wordlist:
        word = line.strip()
        if uses_all(word, enter_letter):
            print (word)
            count += 1
    return count

find_word()

