import random
names_str=input("enter name of the person present seprated by commas ")
name=names_str.split(",")
no_of_persons=len(name)
position_of_person_paying=random.randint(0,no_of_persons-1)
person_paying=name[position_of_person_paying]
print("bill will be payed by"+person_paying)


