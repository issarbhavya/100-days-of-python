ls=[]
tota_std=int(input("enter no. of students "))
for i in range (1,tota_std+1):
    a=int(input(f"enter the marks of student no {i} "))
    ls.append(a)
print(f"\nhighest marks is {max(ls)} ,which is of student no. {ls.index(max(ls))}")
print(f"\nlowest marks is {min(ls)} ,which is of student no. {ls.index(min(ls))}")