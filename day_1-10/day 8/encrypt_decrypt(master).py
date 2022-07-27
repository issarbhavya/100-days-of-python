encrpy=""
decrpy=""
final_str=""
k=0
n=0
shift=0

import string

def enc():
    encrpy=input("enter string for encryption \n")
    encrpy=encrpy.lower()
    shift=int(input("enter values to be shifted by \n"))
    shift%=26
    result=""
    for i in encrpy:
        print(f"{i} is {ord(i)}")
        if ord(i)+shift>122:
            n=ord(i)+shift-122
            i=chr(96+n)
            result=result+i+"*"
        else:
            i=chr(ord(i)+shift)
            result=result+i
    return result

def dec():
    decrpy=input("enter string to be decrypted \n")
    decrpy=decrpy.lower()
    shift=int(input("enter value to be shifted by \n"))
    shift%=26
    result=""
    for i in decrpy:
        print(f"{i} is {ord(i)}")
        if decrpy[decrpy.index(i)+1]=="*":
            n=ord(i)-96
            k=shift-n
            print(n)
            i=chr(122-k)
            print(i)
        elif i=="*":
            i=i
        else:
            i=chr(ord(i)-shift)
        print(f"{i} is {ord(i)}\n\n")
        if (i!="*"):
            result=result+i           
    return result

decision=int(input("enter 1 for encryption nd 2 for decryption  "))
if decision==1:
    final_str=enc()
elif decision==2:
    final_str=dec()
else:
    print("wrong input")
    
print(final_str)
