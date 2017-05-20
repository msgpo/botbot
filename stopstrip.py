""" Strip stop words from text"""
import re

# String to strip of stopwords
needshelp = "How do I make a variable in python?"

stop = open("stopwords.txt", "wr")
words = stop.read()
stopwords = words.strip("\n")
listwords = stopwords.strip("\n")
stop.write(listwords)

query = re.sub("[^\w]", " ",  needshelp).split()
print(query)

if stopwords in query:
	print("STOP!!!")
