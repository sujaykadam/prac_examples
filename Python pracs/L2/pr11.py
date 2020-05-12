#sum of n numbers

num = int(input('Enter an integer '))

if num<0:
    print("Enter positive numbers")
else:
    sum=0
    i=1
    while i<=num:
        sum=sum + i
        i+=1
    print("Sum of",num,"numbers is",sum)
