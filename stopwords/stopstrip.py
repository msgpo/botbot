""" Strip stop words from text"""
import re

class ridstop:
	 
	def __init__(self, question):
		needshelp = str.lower(question)
		self.query = set(re.sub("[^\w]", " ", needshelp).split())
		stop = open("stopwords.txt", "r")
		self.stopwords = set([line.rstrip('\n') for line in stop])

	def stripstop(self):
		goods = self.query.difference(self.stopwords)
		return goods

stuff = ridstop("how do i do stuff")
print(stuff.stripstop())
