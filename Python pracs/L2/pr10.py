#get marks and display grad

m=float(input("Enter marks from 0 to 100 "))

if m>=70:
    print("Grade is DISTINCTION")
elif m>=60:
    print("Grade is FIRST CLASS")
elif m>=50:
    print("Grade is SECOND CLASS")
elif m>=40:
    print("Grade is PASS CLASS")
else:
    print("You have failed")
