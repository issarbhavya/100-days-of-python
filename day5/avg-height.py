c=0
a=int(input(("no. of students ")))
print("enter height of students in sequence in cm")
for i in range (1,a+1):
    c=c+ int(input(f"height of student {i}\n"))
    avg_height=c/a

print(f"\nAvg height is {round(avg_height,2)}")    