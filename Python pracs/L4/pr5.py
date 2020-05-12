#read string display number of digs, lettersand others

s1=input("Enter a string: ")

lc=dc=oc=0
for s in s1:
    if(s.isalpha()):
        lc+=1
    elif(s.isdigit()):
        dc+=1
    else:
        oc+=1

print("There are",lc,"letters",dc,"digits and",oc,"other characters")
