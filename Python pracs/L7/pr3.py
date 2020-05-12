''' maintain score card of players
add, view, update, delete'''

scorecard = {}

while(1):
	op=int(input("1.Add\t\t2.View\n3.Update\t4.Delete\n5.Exit\n\n"))
	if op==1:
		name=input("Enter player name: ")
		runs=int(input("Enter runs scored: "))
		print()
		if scorecard.get(name,-1)==-1:
			scorecard[name]=runs
		else:
			print(name,"already exists")

	elif op==2:
		for n in scorecard:
			print(n,":",scorecard[n])
		print()
	
	elif op==3:
		upplayer=input("Enter player name ")
		newrun=int(input("enter new runs: "))
		scorecard[upplayer]=newrun
	
	elif op==4:
		delplayer=input("Enter player name ")
		if scorecard.get(delplayer,-1)==-1:
			print(delplayer,"does not exist")
		else:
			scorecard.pop(delplayer)
	
	elif op==5:
		break
	
	else:
		print("Invalid option")