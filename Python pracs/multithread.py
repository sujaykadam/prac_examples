import threading
import time
tg=0
for k in range(5):
	fact1=0
	fact2=0
	def factorial(strt,stp,idd):
	    fact=1
	    global fact1
	    global fact2
	    for i in range(strt,stp+1):
	        fact*=i
	    if(idd==1):
	        fact1=fact
	    else:
	        fact2=fact

	thread1 = threading.Thread(target=factorial,args=(1,25000,1,))
	thread2 = threading.Thread(target=factorial,args=(25001,50000,2,))
	t1=time.time()
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	fact=fact1*fact2
	t1=(time.time()-t1)
	print(str(t1))
	tg+=float(t1)
print("\n"+str(tg/5))
