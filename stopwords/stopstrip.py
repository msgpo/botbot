""" Strip stop words from search string"""
import re
<<<<<<< HEAD
"""
# String to strip of stopwords
needshelp = str.lower(input("Enter a search string: "))
# make search string list
query = set(re.sub("[^\w]", " ",  needshelp).split())
print(query)
=======

class ridstop:
	 
	def __init__(self, question):
		needshelp = str.lower(question)
		self.query = set(re.sub("[^\w]", " ", needshelp).split())
		stop = open("stopwords.txt", "r")
		self.stopwords = set([line.rstrip('\n') for line in stop])
>>>>>>> 86b8cb780228d202b69a9e53a7df3b3095b61a90

	def stripstop(self):
		goods = self.query.difference(self.stopwords)
		return goods

<<<<<<< HEAD
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
=======
stuff = ridstop("how do i do stuff")
print(stuff.stripstop())
>>>>>>> 86b8cb780228d202b69a9e53a7df3b3095b61a90
