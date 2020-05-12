# print pattern for n lines
# aaaa
# bbb
# cc
# d

n=int(input("Enter number of lines: "))
ch=97
for i in range(n,0,-1):
        print(i*(chr(ch)+"\t"))
        ch+=1

