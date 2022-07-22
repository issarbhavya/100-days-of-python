height_list=[]
no_of_students=int(input("enter no. of student "))
for i in range (1,no_of_students+1):
    height=int(input(f"Enter height of student no. {i} "))
    height_list.append(height)
sum_of_height=sum(height_list)   
avg_height=sum_of_height/no_of_students
print(avg_height)
