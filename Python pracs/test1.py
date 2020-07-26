lis=list()
n=int(input())
while(n>0):
	lis.append(n)
	n=int(input())
lis.sort(reverse=True)
for i in lis:
	if (i<100):
		print(i)
		break
if (lis[len(lis)-1]>=100):
	print(0)