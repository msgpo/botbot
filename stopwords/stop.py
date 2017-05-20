query = 'How do I make a variable in python?'
stopwords = ['what','who','is','a','at','is','he']
querywords = query.split()
print(querywords)

resultwords  = [word for word in querywords if word.lower() not in stopwords]
result = ' '.join(resultwords)

print(result)
