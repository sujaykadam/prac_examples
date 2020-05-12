#all 3 digit armstrong number

def isarm(num):
    cnum=num
    sum1=0
    while num>0:
        dig=num%10
        sum1=sum1+dig**3
        num=num//10
    if cnum==sum1:
        return True
    else:
        return False

for i in range (100,1000):
    if isarm(i):
        print(i)
        for j in range (0,2000000):
            ss=1+j
    
