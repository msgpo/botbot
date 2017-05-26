""" Strip stop words from search string"""
import re
"""
# String to strip of stopwords
needshelp = str.lower(input("Enter a search string: "))
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
readyGoods = ' '.join(goods)
print(readyGoods)"""


class stripStop():
	"""Strip stopwords from search string"""
	
	def __init__(self, searchQuery, stop="stopwords.txt"):
		"""Gather options for class"""
		self.query = set(re.sub("[^\w]", " ",  searchQuery).split())
		self.stopwords = open(stop, "r");set([line.rstrip('\n') for line in stop])
		
	def stripStop(self):
		"""Rid set of stopwords and turn to string"""
		goods = self.query.difference(stopwords)
		readyGoods = ' '.join(goods)
		#for debuging:
		#print(readyGoods)
		return readyGoods
		
		
striped  = stripStop.stripStop("how do you make a variable in python?")
