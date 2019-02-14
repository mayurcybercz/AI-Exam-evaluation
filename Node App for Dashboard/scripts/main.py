from PIL import Image
import pytesseract
from nltk.stem import WordNetLemmatizer

import removeStop as rs
import userIP as ui
import cosineSim as cs
import spellCheck as sc

def main(path):

    image2 = Image.open(path)
    text = pytesseract.image_to_string(image2, lang="eng")
    print("Your answer as detected by OCR >>> ", text)
    
    processed_data=rs.rmStop(text)

    lemmatizer = WordNetLemmatizer()

    lemmatizedWords = []
    for word in processed_data:
        lemmatizedWords.append(lemmatizer.lemmatize(word.lower()))
        
    keywords = ui.UserIP()
    print("----------------------------------------------------------------------")
    
    lemmatizedWordsString = " ".join(lemmatizedWords)
    keywordsString = " ".join(keywords)

    text1 = lemmatizedWordsString
    text2 =  keywordsString

    vector1 = cs.text_to_vector(text1)
    vector2 = cs.text_to_vector(text2)

    cosine = cs.get_cosine(vector1, vector2)
    
    sc.SpellChecker(lemmatizedWordsString, cosine)
    
if __name__ == '__main__':
    main("testImage2.jpeg")
