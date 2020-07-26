lis=list()
count=0
subseq=list()
n=int(input())
while(n>0):
	lis.append(n)
	n=int(input())
for i in lis:
	if(i%2==1):
		subseq.append(i)
	else:
		for j in subseq:
			if (j>10):
				count+=1
				break
		subseq.clear()
print(count)