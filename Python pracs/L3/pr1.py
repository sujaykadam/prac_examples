#factoril

num=int(input("Enter a number: "))

if num<0:
    print("Enter positive number.")
if num==0 or num==1:
    fact=1
    print("Factorial of",num,"is",fact)
else:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
        print("Factorial of",num,"is",fact)
