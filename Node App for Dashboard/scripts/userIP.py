keywords={}

def UserIP(): # function to take user input
    accepting=True
    while accepting:
        status=input("To enter keyword press Y or press N \n>>> ")
        if(status.lower()=='y'):
            temp_keyword=input("Enter keyword >>> ")
            temp_weightage=int(input("Enter weightage of keyword >>> "))
            keywords[str(temp_keyword)]=temp_weightage
            continue
        elif(status.lower()=='n'):
            accepting=False
    return keywords
