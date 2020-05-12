#implement queue and queue operations

import array as arr
queue=arr.array('i',[])

while(True):
    print("\n1.Add\n2.Remove\n3.Peak\n4.Display\n5.Exit\n")
    op=int(input("Enter option number \n"))

    if op==1:
            ele=int(input("\nEnter element to add\n"))
            queue.append(ele)
            print(ele,"is pushed to queue")

    elif op==2:
        if len(queue)==0:
            print("\nqueue is empty")
        else:
            ele=queue.pop(0)
            print(ele,"is popped from queue")

    elif op==3:
        if len(queue)==0:
            print("\nqueue is empty")
        else:
            ele=queue[0]
            print(ele,"is at the end of the queue")
    elif op==4:
        if len(queue)==0:
            print("\nqueue is empty")
        else:
            for i in queue:
                print( i,end="\t")
            print() 
    elif op==5:
        break
    else:
        print("\nInvalid option")
