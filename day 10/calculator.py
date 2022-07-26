
def add(a,b):
    sum=a+b
    return sum
       
def sub(a,b):
    diff=abs(a-b)
    return diff  
 
def mul(a,b):
    multi=a*b
    return multi 
  
def div(a,b):
    divi=a/b
    return int(divi)

result=0
decision="n"
while decision=="n" or "c":
    if(decision=="c"):
        a=result
        print(f"number 1 is : {a}\n")
    elif(decision=="n"):
        a=int(input("enter number 1: "))
    command=input(""" pick an operation :
                  +
                  -
                  *
                  / 
                  :""")
    b=int(input("enter number 2: "))
    calc={"+":add(a,b),"-":sub(a,b),"*":mul(a,b),"/":div(a,b)}
    result=calc[command]
    print(f"{a} {command} {b} = {result}")
    decision=input("""type \"c\" to contuinue
        Enter \"n\" to begin begin new calculation
        Press any other key to terminate 
        : """ )
    
        
        
    

    
    
    
    