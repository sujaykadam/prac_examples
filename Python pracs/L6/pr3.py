#menu driven function area

def area(num1=None,num2=None):
    if num1 is not None and num2 is None:
        ar=3.14*num1**2
    elif num1 is not None and num2 is not None:
        ar=num1*num2
    return ar
while(1):
    op=int(input("1.Area of circle\n2.Area of rectangle\n3.Exit\n"))

    if op==1:
        print("Area of circle is:",area(float(input("Enter radius: "))))
    elif op==2:
        print("Area of rectangle is:",area((float(input("Enter length : "))),(float(input("Enter width : ")))))
    elif op==3:
        break
    else:
        print("Invalid option")
