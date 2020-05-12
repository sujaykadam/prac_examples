#count vovels and consonents

s1=input("Enter a string: ")

vc=cc=0

for i in s1 :
    if i.isalpha():
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
            vc+=1
        else:
            cc+=1

print("There are",vc,"vovels and",cc,"consonents in",s1)
