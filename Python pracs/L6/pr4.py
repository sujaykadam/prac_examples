#myrange() pass 1 and 2 arg
#myrange(4)= 1,2,3,4
#myrange(2,4)= 2,3,4

def myrange(n1=None,n2=None):
    if n1 is not None and n2 is None:
        start=1
        while start<=n1:
            print(start)
            start+=1
    elif n1 is not None and n2 is not None:
        start,stop=n1,n2
        while start<=stop:
            print(start)
            start+=1
myrange(4,10)
