#read list of marks and print high low
num=[]

rep='y'
while rep=='y':
    ele=int(input("Enter marks"))
    num.append(ele)
    rep=input("add int?")
num.sort()
nn=num[-1]
nl=num[0]
print("high=",nn,"low=",nl)

