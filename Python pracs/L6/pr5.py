#read list of integers  and print

num=[]

rep='y'
while rep=='y':
    ele=int(input("Enter int"))
    num.append(ele)
    rep=input("add int?")
print (num)
for n in num:
    print(n,end=" ")
print()
