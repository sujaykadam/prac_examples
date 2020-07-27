n=int(input("Enter number of elements: "))
lis=list()
for i in range(n):
	lis.append(int(input("Enter element "+str(i+1)+": ")))

def merge(lis, l,m,r):
	i,j=l,m+1
	n1,n2=m,r
	srt=list()
	while(i<=n1 and j<=n2):
		if(lis[i]<lis[j]):
			srt.append(lis[i])
			i+=1
		else:
			srt.append(lis[j])
			j+=1
	while (i<=n1):
		srt.append(lis[i])
		i+=1
	while (j<=n1):
		srt.append(lis[j])
		j+=1
	m=l
	for k in srt:
		lis[m]=k
		m+=1

def mergesort(lis,l,r):
	if(l<r):
		m=(l+r)//2
		mergesort(lis,l,m)
		mergesort(lis,m+1,r)
		merge(lis,l,m,r)
mergesort(lis,0,n-1)
print(lis)