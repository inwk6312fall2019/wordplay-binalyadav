'''Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?'''



def is_abecedarian(word):
    first_letter = word[0]
    second_letter = word[1]
    letter_index = 1

    while letter_index  (second_letter):
    	return False
        first_letter = second_letter
        letter_index += 1
        second_letter = word[letter_index]
    return True

myfile = open("words.txt")

def calculate_abecedarian():
    total = 0
    for word in myfile:
        if is_abecedarian(word):
            print (word)
            total += 1
    return total

calculate_abecedarian()