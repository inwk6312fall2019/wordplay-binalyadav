'''Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).'''

myfile = open('words.txt')
for line in myfile:
	word = line.strip()
	if len(word) > 20:
		print (word)