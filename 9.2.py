'''In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
does not contain the letter “e.” Since “e” is the most common letter in English, that’s not easy to
do.
Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
it.'''

myfile = open("words.txt")

def has_no_e(word):
    for char in word:
        if char in 'e':
            return False
    return True  



'''Modify your program from the previous section to print only the words that have no “e” and compute
the percentage of the words in the list have no “e.”'''


myfile = open("words.txt")

def has_no_e():
    total= 0
    no_e= 0

    for line in myfile:
        word = line.strip()
        if "e" not in word:
            no_e += 1
            print (word)
        total += 1

    percentage = float(no_e) / total* 100
    return percentage
has_no_e()