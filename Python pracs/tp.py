#recursive sum of digits

def sod(num):
    if num==0:
        return 0
    else:
        return (num%10) + sod(num//10)

print(sod(int(input("Enter number"))))
