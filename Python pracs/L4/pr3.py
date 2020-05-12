#implement stack and stack operations

import array as arr
stack=arr.array('i',[])

while(True):
    print("\n1.Push\n2.Pop\n3.Peak\n4.Display\n5.Exit\n")
    op=int(input("Enter option number \n"))

    if op==1:
            ele=int(input("\nEnter element to push\n"))
            stack.append(ele)
            print(ele,"is pushed to stack")

    elif op==2:
        if len(stack)==0:
            print("\nStack underflow")
        else:
            ele=stack.pop()
            print(ele,"is popped from stack")

    elif op==3:
        if len(stack)==0:
            print("\nStack underflow")
        else:
            ele=stack[-1]
            print(ele,"is at the top of the stack")
    elif op==4:
        if len(stack)==0:
            print("\nStack underflow")
        else:
            for i in stack:
                print("\n",i,end="\t")
    elif op==5:
        break
    else:
        print("\nInvalid option")
