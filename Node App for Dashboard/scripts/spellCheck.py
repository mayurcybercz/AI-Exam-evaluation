import enchant
import tokenizer as tk
import score as sc
dictionary = enchant.Dict("en_US")   # create dictionary for US English

def SpellChecker(line,cosine):
    for token in tk.tokens(line):
        spellMistakes=0
        strippedToken=token.rstrip()
        if(dictionary.check(strippedToken)==False):
            spellMistakes = spellMistakes+1
    print("Spelling mistakes >>>",spellMistakes)
    sc.Score(cosine, spellMistakes)
