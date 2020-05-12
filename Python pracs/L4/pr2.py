#sort asd and dec and menu driven

import array as arr
data=arr.array('i',[])

n=int(input("Enter number of elements "))

for i in range(n):
    data.append(int(input("Enter the element ")))

copy=data
while(True):
    print("\n\n1.Show array\n2.Show array in ascending order\n3.Show data in decending order\n4.Exit\n")
    op=int(input("Enter option number "))

    if op==1:
        print("\nArray is")
        for d in data:
            print(d,end="\t")
    elif op==2:
        copy=sorted(data)
        print("\nArray in ascending order is ")
        for d in copy:
            print(d,end="\t")
    elif op==3:
        copy=sorted(data, reverse=True)
        print("\nArray in ascending order is ")
        for d in copy:
            print(d,end="\t")
    elif op==4:
        break
    else:
        print("\nGive valid option \n\n")
