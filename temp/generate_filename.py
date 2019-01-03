from datetime import datetime

def replaceMultiple(mainString, toBeReplaces, newString):
   
    for elem in toBeReplaces :
        
        if elem in mainString :
            
            mainString = mainString.replace(elem, newString)
    
    return  mainString

mainStr=str(datetime.now())
file_name = replaceMultiple(mainStr, [':', '-', '.',' '] , "")

def generateFilename():
	mainStr=str(datetime.now())
	file_name = replaceMultiple(mainStr, [':', '-', '.',' '] , "")
	return file_name
