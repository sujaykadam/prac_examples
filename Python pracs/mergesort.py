'''
n=int(input("Enter number of elements: "))
lis=list()
for i in range(n):
	lis.append(int(input("Enter element "+str(i+1)+": ")))
'''
lis=list()
lis=[9,0,5,1,8,3,7,2,6,4]

def merge(lis,l,m,r):
	i=l
	j=m
	n1=m-1-l
	n2=r-m
	temp=list()
	while(i<=n1 and j<=n2):
		if(lis[i]<lis[j]):
			temp.append(lis[i])
			i+=1
		else:
			temp.append(lis[j])
			j+=1
	while(i<=n1):
		temp.append(lis[i])
		i+=1
	while(j<=n2):
		temp.append(lis[j])
		j+=1
	for k in range(len(temp)):
		lis[l+k]=temp[k]
	print("merge"+(str([l,m,r])))
def mergesort(lis,l,r):
	if(l<r):
		m=(l+r)//2
		print(l,m,r)
		mergesort(lis,l,m)
		mergesort(lis,m+1,r)
		merge(lis,l,m,r)

mergesort(lis,0,9)
print(lis)