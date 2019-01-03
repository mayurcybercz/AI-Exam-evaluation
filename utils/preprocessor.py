from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

data = "Conductor in magnetic field produces voltage."

#remove stopwords

def rmStop(data):
	stopWords=set(stopwords.words('english'))
	words=word_tokenize(data)
	wordsFiltered=[]
	for w in words:
		if w not in stopWords:
			wordsFiltered.append(w)
	return wordsFiltered