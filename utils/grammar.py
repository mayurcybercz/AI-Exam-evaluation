accepting=True
titles={}
totalMistakes=0

#titles are to be written with uppercase starting letter

while accepting:
	status=input("To enter title press Y or press N \n")
	if status.lower()=='y':
		temp_title=input("Enter title")
		temp_weightage=int(input("Enter weightage of title correctness"))
		titles[str(temp_title)]=temp_weightage
			continue
	else if status.lower()=='n':
		accepting=False

def check_titles(sample_string):
	if not ( (sample_string in Titles) and (sample_string.istitle())):
		totalMistakes=totalMistakes+ (1* titles[str(title)])
