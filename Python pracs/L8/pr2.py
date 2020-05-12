#oopp for class circle

class circle:
	def __init__(self,r):
		self.r=r

	def display(self):
		print("Radius: ",self.r)

	def area(self):
		area=round(self.r**2*3.14,2)
		print("Area: ",area)

	def circ(self):
		circ=round(2*3.14*self.r,2)
		print("Circumference: ",circ)

r=float(input("Enter radius: "))
cir=circle(r)
cir.display()
cir.area()
cir.circ()