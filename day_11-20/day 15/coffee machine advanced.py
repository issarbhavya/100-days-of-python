from pickle import GLOBAL
from secrets import choice

code="1111"

menu = {
      "espresso": {"ingredients": {"water": 50,"milk":0,"coffee": 18,},"cost": 1.5,},
    "latte": {"ingredients": {"water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino": {"ingredients": {"water": 250,"milk": 100,"coffee": 24,},"cost": 3.0,}
}
resources = {
    "water": 600,
    "milk": 250,
    "coffee": 300,
}
coins={
    "penny":0.01,
       "nickle":0.05,
       "dime":0.10,
       "quarter":0.25
       }

money_in_machine=0

def avaliable_in_menu():
    avaliable_items=[]
    global menu
    global resources
    requirements=""
    for order in menu:
        requirements=menu[order]
        ingredients=requirements["ingredients"]
        c=0
        for items in ingredients:
            if ingredients[items]<=resources[items]:
                c+=1
        if(c==3):
            avaliable_items.append(order)
        else:
            print(f"resources are not suffecient for {order}")
    return avaliable_items

  
def check_amount_paid(amount):
    global money_in_machine
    print(f"\namount to be paid is : ${amount}")
    amount=float(amount)
    no_of_penny=int(input("enter no. of pennies deposited : "))
    no_of_nickle=int(input("enter no. of nickle deposited : "))
    no_of_dime=int(input("enter no. of dime deposited : "))
    no_of_quarter=int(input("enter no. of quarter deposited : "))
    inputed_amount=(no_of_penny*0.01)+(no_of_nickle*0.05)+(no_of_dime*0.10)+(no_of_quarter*0.25)
    money_in_machine+=inputed_amount
    if(inputed_amount>=amount):
        print("Payment completed\n")
        return True
    else:
        print("\n\n")
        shortage=amount-inputed_amount
        print(f"you are ${shortage} less\n\n")
        decision=input(f"press y to add the shortage amount of {shortage}\n\nElse press n to take back your money: ")
        if (decision=="y"):
            check_amount_paid(shortage)
        elif(decision=="n"):
            return False

def coffee(name_of_coffee):
    user_input=menu[name_of_coffee]
    ingredients_required=user_input["ingredients"]
    cost=user_input["cost"]
    if not (check_amount_paid(cost)==False):
        resources["water"]-=ingredients_required["water"]
        resources["milk"]-=ingredients_required["milk"]
        resources["coffee"]-=ingredients_required["coffee"]
        print(f"\n\nHERE IS YOUR {name_of_coffee}, THANKS AND VISIT AGAIN")
    else:
        print("you were not able to pay the required amount so here's the amount you paid\n\n")



machine_is_off=False
while(machine_is_off==False):
    print("\n\nHELLO CUSTOMER \n")
    lst_of_avaliability=avaliable_in_menu()
    
    if(len(lst_of_avaliability)==0):
        print("\nSorry we are not taking orders due to shortage of resources")
        machine_is_off=True
        break
    
    print("\nOur menu is: espresso/latte/cappuccino")
    print("\nCurrent avaliable items are as foloows: ")
    
    for items in lst_of_avaliability:
        print(f"\n{items}")
    choice_of_coffee_made=input("\npls enter your order : ")

    if choice_of_coffee_made=="report":
        code_entered=input("enter the machine code : ")
        print("\n\n")
        if(code==code_entered):
            print(f"""the report till now is :
        resoursec left : {resources}
        amount earned till now is ${money_in_machine}\n\n""")
            decision=input("press \"off\" to switch off the machine else press any other key to continue : ")
            if(decision=="off"):
                print("\n\nThanks, hope to see you again owner")
                machine_is_off=True
        else:
            print("wrong code\n")
    else:
        coffee(choice_of_coffee_made)  