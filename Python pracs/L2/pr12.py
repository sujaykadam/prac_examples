#sum of digits

num = int(input("Enter an integer "))
copy=num
if num<0:
    print("Enter positive number")
else:
    sum = 0
    while num>0:
        dig=num%10
        sum=sum+dig
        num=num//10
    print("Sum of digits of",copy,"is",sum)
