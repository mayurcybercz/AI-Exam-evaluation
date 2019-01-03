from pytesseract import pytesseract
import generate_filename as gf
import sys
import os

pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract'


def createHOCR(imagepath):
	filename= gf.generateFilename()
	pytesseract.run_tesseract(imagepath, filename, lang=None,extension='html', config="hocr")
	print("HOCR file generated: "+str(filename)+".hocr")

if __name__ == "__main__":
	cwd=str(os.getcwd()).replace("scripts","images")+"\\"
	createHOCR(cwd+str(sys.argv[1]))