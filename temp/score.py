def Score(cosine, spellMistakes):
    score = 1
    if cosine*100 > 80:
        score = score - ( 0.05 * spellMistakes)
    else: 
        score = 0
        print("Output >>> inaccurate answer")
    print("Cosine >>> ",cosine)
    print("Score >>> ",score)
