from pytesseract import pytesseract
import generate_filename as gf
import sys
import os

#Edit path to tesseract executable if you installation directory changed

pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

def createHOCR(imagepath):
	filename= gf.generateFilename()
	pytesseract.run_tesseract(imagepath, filename, lang=None,extension='html', config="hocr")
	print("HOCR file generated: "+str(filename)+".hocr")

if __name__ == "__main__":
	cwd=str(os.getcwd()).replace("scripts","images")+"\\"
	createHOCR(cwd+str(sys.argv[1]))
