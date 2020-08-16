from PIL import Image
import os

def main(): 
	try: 
		#Relative Path 
		image1 = Image.open('image1.jpeg') 
		image2 = Image.open('image2.jpeg') 
		
		#Getting histogram of image 
		print (image1.histogram())
		h1 = (image1.histogram())
		h2 = (image2.histogram())
		#print (h1)
		#print (h1)
		
		if (h1==h2):
			os.remove('image2.jpeg')
			print("Duplicate Found!! \n Deleted Successfully")
		else:
			print("No Duplicates are Found")
	except IOError: 
		pass




if __name__ == "__main__": 
	main() 
