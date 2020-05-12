#count number of occurrences of a char in i/p string

s1=input("Enter a string: ")

countletter={}

for s in s1:
	ans = countletter.get(s,-1)
	if ans == -1:
		countletter[s] = 1
	else:
		countletter[s] = ans+1

print(countletter)