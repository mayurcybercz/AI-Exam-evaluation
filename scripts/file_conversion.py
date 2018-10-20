from lxml import etree
import pandas as pd
import os
import sys
import generate_filename as gf



def hocr_to_dataframe(fp):

    doc = etree.parse(fp)
    words = []
    wordConf = []

    for path in doc.xpath('//*'):
        if 'ocrx_word' in path.values():
            conf = [x for x in path.values() if 'x_wconf' in x][0]
            wordConf.append(int(conf.split('x_wconf ')[1]))
            words.append(path.text)

    dfReturn = pd.DataFrame({'word' : words,
                             'confidence' : wordConf})

    return(dfReturn)


if __name__ == "__main__":
    filename=gf.generateFilename()

    #generating dataframe from HOCR file

    dataframe=hocr_to_dataframe(str(sys.argv[1]))

    #generating JSON and Pickle files from dataframe
    
    dataframe.to_json(filename+".json",orient='columns')
    print("JSON generated: "filename+".JSON")
    dataframe.to_pickle(filename+".pkl")
    print("Pickle generated: "filename+".pkl")

