#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"

student_score={}
student_grade={}
num_std=int(input("enter no. of students :"))
for i in range (0,num_std):
    name=input(f"enter name of student no. {i+1} : ")
    marks=int(input("enter marks of the student :\n"))
    student_score[name]=marks
    if(marks>90):
        grade="outstanding"
    elif (marks>80 and marks<90):
        grade="exceeeds expectations"
    elif (marks>70 and marks<80):
        grade="acceptable"
    else:
        grade="fail"
    student_grade[name]=grade
print(student_score)
print(student_grade)