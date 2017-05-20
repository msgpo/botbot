""" This takes a words and then changes them into a list - 1 object per line"""
stop = open("stopwords.txt", "r")

# If you don't want to strip the \n uncomment and comment the next words assinment below
#words = list(stop)

words = [line.rstrip('\n') for line in stop]

print(words)
