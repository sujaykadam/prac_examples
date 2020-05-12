#armstrong number 3digits

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

print("\n",isarm(int(input("Enter number "))))
