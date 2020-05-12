#bill generations

menu={'idli':20,'vada':30,'dosa':25}
amount=0.0
while (1):
	op= int(input("1.ADD\t2.Amount\n3.Exit\n\n"))
	if op==1:
		name=input("Enter item name ")
		if menu.get(name,-1)!=-1:
			q=float(input("Enter quantity: "))
			amount=amount+((int(menu.get(name)))*q)
		else:
			print("\nitem non\n")
		
	elif op==2:
		print(amount)

	elif op==3:
		break

	else:
		print("invalid option")
