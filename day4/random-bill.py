import random
names_str=input("enter name of the persons present seprated by commas ")
name=names_str.split(",")
no_of_persons=len(name)
position_of_person_paying=random.choice(name)
print("bill will be payed by "+position_of_person_paying)


