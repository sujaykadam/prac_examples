#menu driven oj oriented for employee

class employee:
	ecount=0
	def __init__(self,eid,ename,esalary):
		self.eid=eid
		self.ename=ename
		self.esalary=esalary
		employee.ecount+=1

	def show(self):
		print("EID: ",self.eid)
		print("Employee name: ",self.ename)
		print("Salary: ",self.esalary)
		
	def calc_bonus(self):
		ans=self.esalary*0.1
		print("Bonus: ",ans)

	@staticmethod
	def showecount():
		print("Ecount: ",employee.ecount)

emp=[]

while 1:
	op=int(input("\n1.ADD\t\t2.View\n3.Delete\t4.Exit\n"))

	if op==1:
		eid=int(input("Enter EID: "))
		ename= input("Enter employee name: ")
		esalary=int(input("Enter salary: "))
		e=employee(eid,ename,esalary)
		emp.append(e)

	elif op==2:
		e.showecount()
		for e in emp:
			print("*-"*20)
			employee.show(e)
		print("*-"*20)
					
	elif op==3:
		eid=int(input("Enter EID: "))
		for e in emp:
			if e.eid==eid:
				emp.remove(e)
				employee.ecount-=1
		
	elif op==4:
		break

	else:
		print("Invalid option\n")
