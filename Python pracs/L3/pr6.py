#read n marks find avg marks,highest, lowest, studs with marks >=70, <=40

import array as arr

n=int(input("Enter number of students: "))
marks=arr.array('i',[])

for i in range (n):
    m=int(input("Enter marks: "))
    marks.append(m)

sum=0
for m in marks:
    sum=sum+m
avg=sum/n
print("Average of marks is: ",avg)

max=0
min=marks[1]
for i in range(n):
    if max<=marks[i]:
        max=marks[i]
for i in range(n):
    if min>=marks[i] :
        min=marks[i]
print("Higest marks are",max,"lowest marks are",min)

_70=_40=0
for i in range(n):
    if marks[i]>=70:
        _70+=1
    elif marks[i]<=40:
        _40+=1
print("Students with >=70 are",_70,"and <=40 are",_40)



