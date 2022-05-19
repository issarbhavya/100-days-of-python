year = int(input("Which year do you want to check? "))


if(year%4==0 ):
    c=1;
    if(year%100==0):
        c=0;
        if(year%400==0):
            c=1;
else:
    c=0;
    
if(c==1):
    print("Leap year.")
else:
    print("Not leap year.")