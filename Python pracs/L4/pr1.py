#read array of n integers and count +ve and -Ve int and 0s

import array as arr
data=arr.array('i',[])

n=int(input("Enter number of elements "))

for i in range(n):
    data.append(int(input("Enter the element ")))

z=p=n=0
for j in data:
    if j<0:
        n=n+1
    elif j>0:
        p=p+1
    else:
        z=z+1

print("Number of positive elements is",p,", negetive elements is",n,"and zeros is",z)  
    
