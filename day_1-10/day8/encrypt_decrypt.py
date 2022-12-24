encrpy=""
decrpy=""
shift=0
final_str=""
import string

def enc():
    encrpy=input("enter string for encryption \n")
    encrpy=encrpy.lower()
    shift=int(input("enter values to be shifted by \n"))
    result=""
    for i in encrpy:
        i=chr(ord(i)+shift)
        result=result+i
    return result

def dec():
    decrpy=input("enter string to be decrypted \n")
    decrpy=decrpy.lower()
    shift=int(input("enter value to be shifted by \n"))
    result=""
    for i in decrpy:
        i=chr(ord(i)-shift)
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

    
        
    