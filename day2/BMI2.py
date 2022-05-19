import math
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi= weight/(height*height)
bmi=math.ceil(bmi)

if(bmi<18.5):
    c=", you are underwieght."
if(bmi>18.5 and bmi<25):
    c=", you have a normal weight."
if(bmi>25 and bmi<30):
    c=", you are slightly overweight."
if(bmi>30 and bmi<35):
    c=", you are obese."
if(bmi>35):
    c=", you are clinically obese."

bmi= str(bmi);
print("Your BMI is "+ bmi + c)    
