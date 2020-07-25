import time
tg=0
for k in range(5):
	factor=1
	t1=time.time()
	for i in range(1,50001):
	    factor*=i
	t1=(time.time()-t1)
	print(str(t1))
	tg+=float(t1)
print(tg/5)