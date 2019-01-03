import preprocessor as pp


accepting=True
keywords={}
totalMarks=0
sample_question="explain the types of computer"
sample_string ="super computer mainframe computer mini computer"
processed_data=pp.rmStop(sample_string)

while accepting:
	status=input("To enter keyword press Y or press N \n")
	if status.lower()=='y':
		temp_keyword=input("Enter keyword")
		temp_weightage=int(input("Enter weightage of keyword"))
		keywords[str(temp_keyword)]=temp_weightage
			continue
	else if status.lower()=='n':
		accepting=False

#print(keywords)
# add super:1 , mainframe:1,mini:1

for keyword in keywords.keys():
	if keyword in processed_data:
		totalMarks=totalMarks+ (1* keywords[str(keyword)])




