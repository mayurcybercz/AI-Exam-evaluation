#Cropping Functionality for images
from PIL import Image
import pytesseract
from IPython.display import display
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

im = Image.open("download.jpg")
fig, ax = plt.subplots()
ax.imshow(im)
print("(width,height):"+str(im.size))
text = pytesseract.image_to_string(im, lang = 'eng')
print(text)

top_left_x=int(input("Enter x co-ordinate of top left vertice to crop : "))
top_left_y=int(input("Enter y co-ordinate of top left vertice to crop : "))
bottom_right_x=int(input("Enter x co-ordinate of bottom right vertice to crop : "))
bottom_right_y=int(input("Enter y co-ordinate of bottom right vertice to crop : "))

box = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
cropped_image = im.crop(box)
display(cropped_image)
cropped_text= pytesseract.image_to_string(cropped_image, lang = 'eng')
print(cropped_text)