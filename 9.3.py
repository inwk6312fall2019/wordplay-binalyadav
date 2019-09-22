'''Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then print the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?'''

my_file = open("words.txt")

def avoids(word, string):
    for char in string:
        if char in word:
            return False
    return True

def num_of_words():
    count = 0
    avoid = input("enter the string:")
    avoid = avoid.lower()

    for line in my_file:
        word = line.strip()
        if avoids(word, avoid):
            count += 1
    return count
print(num_of_words())