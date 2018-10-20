CLI-Tool to recognise handwritten text from answer sheets using Tesseract OCR.
Using this extracted text to evaluate marks using NLP.

Installation:
Install Tesseract-OCR-Engine https://github.com/tesseract-ocr/tesseract/wiki
Install python dependencies pytesseract,pillow,pandas,numpy,matplotlib

Usage:
1)Clone the repository into your working directory
2)Make sure you update path of tesseract executable in main.py
3)add image for testing to images folder
4)main.py imagename
It will return a HOCR file,which is very similar to XHTML
5)file_conversion.py hocrfilename.
It will convert HOCR into dataframe and store the output in a pickle file/json file



Phase1 demonstration of the OCR of handwritten text and exploiting into JSON
(Rendered python notebook displayed as markdown using nbconvert)

```python
from pytesseract import pytesseract
import sys
import os
```


```python
#Edit path to tesseract executable if you installation directory changed

pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
```


```python
from datetime import datetime

def replaceMultiple(mainString, toBeReplaces, newString):
   
    for elem in toBeReplaces :
        
        if elem in mainString :
            
            mainString = mainString.replace(elem, newString)
    
    return  mainString

mainStr=str(datetime.now())
file_name = replaceMultiple(mainStr, [':', '-', '.',' '] , "")
```


```python
def generateFilename():
	mainStr=str(datetime.now())
	file_name = replaceMultiple(mainStr, [':', '-', '.',' '] , "")
	return file_name
```


```python
from PIL import Image
from IPython.display import display
import matplotlib.pyplot as plt

im = Image.open("testfile1.jpg")
fig, ax = plt.subplots()
ax.imshow(im)
print("(width,height):"+str(im.size))
```

    (width,height):(3000, 3115)
    


```python
box=(250,180,2800,400)
cropped_image = im.crop(box)
display(cropped_image)
cropped_text= pytesseract.image_to_string(cropped_image, lang = 'eng')
print(cropped_text)
```


![png](demonstration_files/demonstration_5_0.png)


    Conductor wn magnetic Field Produce voltage :
    


```python
def createHOCR(imagepath):
	filename= generateFilename()
	pytesseract.run_tesseract(imagepath, filename, lang=None,extension='html', config="hocr")
	print("HOCR file generated: "+str(filename)+".hocr")
```


```python
createHOCR("testfile.jpg")
```

    HOCR file generated: 20181021042317089205.hocr
    


```python
from lxml import etree
import pandas as pd
import os
import sys
import generate_filename as gf
```


```python
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
```


```python
filename=generateFilename()
dataframe=hocr_to_dataframe("20181021041156998790.hocr")
```


```python
dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>confidence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td></td>
      <td>95</td>
    </tr>
    <tr>
      <th>1</th>
      <td></td>
      <td>95</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Q1.</td>
      <td>89</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Define</td>
      <td>96</td>
    </tr>
    <tr>
      <th>4</th>
      <td>electromagnetic</td>
      <td>96</td>
    </tr>
    <tr>
      <th>5</th>
      <td>induction.</td>
      <td>95</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Sane</td>
      <td>23</td>
    </tr>
    <tr>
      <th>7</th>
      <td>|</td>
      <td>90</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Conductor</td>
      <td>93</td>
    </tr>
    <tr>
      <th>9</th>
      <td>mM</td>
      <td>42</td>
    </tr>
    <tr>
      <th>10</th>
      <td>magnetic</td>
      <td>70</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Field</td>
      <td>63</td>
    </tr>
    <tr>
      <th>12</th>
      <td>produce</td>
      <td>67</td>
    </tr>
    <tr>
      <th>13</th>
      <td>voltage</td>
      <td>65</td>
    </tr>
    <tr>
      <th>14</th>
      <td>‘Seconaewctntmnstnn</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>esionainsnenaneenrenncconanniiti</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Q2.</td>
      <td>89</td>
    </tr>
    <tr>
      <th>17</th>
      <td>What</td>
      <td>96</td>
    </tr>
    <tr>
      <th>18</th>
      <td>are</td>
      <td>96</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3</td>
      <td>96</td>
    </tr>
    <tr>
      <th>20</th>
      <td>examples</td>
      <td>96</td>
    </tr>
    <tr>
      <th>21</th>
      <td>of</td>
      <td>95</td>
    </tr>
    <tr>
      <th>22</th>
      <td>transparent</td>
      <td>95</td>
    </tr>
    <tr>
      <th>23</th>
      <td>objects?</td>
      <td>96</td>
    </tr>
    <tr>
      <th>24</th>
      <td>(Professor</td>
      <td>96</td>
    </tr>
    <tr>
      <th>25</th>
      <td>provides</td>
      <td>96</td>
    </tr>
    <tr>
      <th>26</th>
      <td>5</td>
      <td>96</td>
    </tr>
    <tr>
      <th>27</th>
      <td>as</td>
      <td>95</td>
    </tr>
    <tr>
      <th>28</th>
      <td>input)</td>
      <td>90</td>
    </tr>
    <tr>
      <th>29</th>
      <td></td>
      <td>95</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Q3.</td>
      <td>92</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Complete</td>
      <td>96</td>
    </tr>
    <tr>
      <th>32</th>
      <td>the</td>
      <td>96</td>
    </tr>
    <tr>
      <th>33</th>
      <td>network</td>
      <td>95</td>
    </tr>
    <tr>
      <th>34</th>
      <td>tree.</td>
      <td>96</td>
    </tr>
    <tr>
      <th>35</th>
      <td></td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataframe.to_json(filename+".json",orient='columns')
print("JSON generated: "+filename+".JSON")
dataframe.to_pickle(filename+".pkl")
print("Pickle generated: "+filename+".pkl")
```

    JSON generated: 20181021042319190731.JSON
    Pickle generated: 20181021042319190731.pkl
    
