#oopp for rectangle

class rectangle:
	def __init__(self, leng, wid):
		self.leng= leng
		self.wid= wid

	def show(self):
		print("Length=",self.leng,"width=",self.wid)

	def area(self):
		area=self.leng*self.wid
		print("Area=",area)

	def peri(self):
		peri=(self.leng+self.wid)*2
		print("Perimeter= ",peri)

leng=float(input("Enter length: "))
wid=float(input("Enter width: "))

rect = rectangle(leng,wid)
rect.show()
rect.area()
rect.peri()
