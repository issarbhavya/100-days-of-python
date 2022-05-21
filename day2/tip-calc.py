print ("welcome to the tip calculator")
bill= float(input("what was the total bill? $"))
tip_percent=int(input("what percentage of tip would you like to give 10 or 12 or 15? "))
no_of_people=int(input("how many people to split the bill? "))

tip=tip_percent/100*bill
total_amount=bill+tip
single_share=round(total_amount/no_of_people ,2)

print (f"each person should pay: ${single_share}")