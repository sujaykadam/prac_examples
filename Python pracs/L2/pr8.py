#read 3 int and find max

n1=int(input("Enter first number "))
n2=int(input("Enter second number "))
n3=int(input("Enter third number "))

if(n1>n2):
    max=n1
else:
    max=n2

if(max<n3):
    max=n3

print("Max of",n1,n2,n3,"is",max)
