#palindrome

s1=input("Enter string to check if palindrome: ")
s2=s1.lower()

s3=s2[::-1]

if s3==s2:
    print("Entered string is palindrome.")
else:
    print("Entered string is not palindrome.")
