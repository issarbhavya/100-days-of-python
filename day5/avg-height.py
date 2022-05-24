c=0
a=int(input(("no. of students ")))
print("enter height of students in sequence in cm")
for i in range (0,a):
    c=c+ int(input("\n"))
    avg_height=c/a

print(f"\nAvg height is {avg_height}")    