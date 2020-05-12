#generate pattern for n lines
# A
# BB
# CCC
# DDDD

n=int(input("Enter number of lines: "))
val=65
for i in range(1,n+1):
        print(i*((chr(val)+"\t")))
        val = val+1
        
