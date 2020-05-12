#usernamer and pass verification

import getpass

s1="antman"
s2="batman"

while(1):
    s3=input("Enter username: ")
    s4=getpass.getpass("Enter password: ")

    if s1==s3 and s2==s4:
        print("WELCOME")
        break
    else:
        print("TRY AGAIN")
