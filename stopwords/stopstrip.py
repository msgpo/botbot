""" Strip stop words from text"""
import re

# String to strip of stopwords
needshelp = "him"
# make search string list
query = set(re.sub("[^\w]", " ",  needshelp).split())
print(query)

# Open and make file list
stop = open("stopwords.txt", "r")
stopwords = set([line.rstrip('\n') for line in stop])
print(stopwords)

if query.intersection(stopwords):
	print("YESSS!!!")
