""" Strip stop words from text"""
import re

# String to strip of stopwords
needshelp = str.lower("how do I make a variable in python?")
# make search string list
query = set(re.sub("[^\w]", " ",  needshelp).split())
print(query)

# Open and make file list
stop = open("stopwords.txt", "r")
stopwords = set([line.rstrip('\n') for line in stop])
print(stopwords)
print("\n") # Make a space in between lines of code

# find and recreate string
goods = query.difference(stopwords)
print(goods)
