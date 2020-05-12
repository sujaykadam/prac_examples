#wapp to read tuple of ints from user and display in descndeing order
list_number=[]

reply='y'
while reply=='y':
	m = int(input('Enter integer '))
	list_number.append(m)
	reply = input ('Do yo wish to add  more marks y/n ')
list_number.sort(reverse=True)

tup=tuple(list_number)

print(tup)

