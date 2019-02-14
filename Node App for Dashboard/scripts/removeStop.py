from nltk.corpus import stopwords
import tokenizer as tk

def rmStop(data): # function to remove stop words
    stopWords=set(stopwords.words('english'))
    words=tk.tokens(data)
    wordsFiltered=[]
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)
    return wordsFiltered
