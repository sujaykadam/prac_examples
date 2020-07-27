n=int(input("Enter number of elements: "))
lis=list()
for i in range(n):
	lis.append(int(input("Enter element "+str(i+1)+": ")))

def swap(i,j):
	lis[i],lis[j]=lis[j],lis[i]

def partition(lis,left,right):
	i=left
	pivot=lis[right]
	j=right-1
	while(i<j):
		while(lis[i]<=pivot and i<=j):
			i+=1
		while(lis[j]>pivot):
			j-=1
		if(i<j):
			swap(i,j)
	swap(i,right)
	return i

def quicksort(lis, left, right):
	if(left<right):
		pos=partition(lis, left, right)
		quicksort(lis,left,pos-1)
		quicksort(lis,pos+1,right)

quicksort(lis,0,n-1)
print(lis)
