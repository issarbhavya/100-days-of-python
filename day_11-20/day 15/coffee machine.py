from pickle import GLOBAL
from secrets import choice

code="coffee chahiye"

menu = {
      "espresso": {"ingredients": {"water": 50,"milk":0,"coffee": 18,},"cost": 1.5,},
    "latte": {"ingredients": {"water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino": {"ingredients": {"water": 250,"milk": 100,"coffee": 24,},"cost": 3.0,}
}

resources = {
    "water": 600,
    "milk": 600,
    "coffee": 300,
}

coins={
    "penny":0.01,
       "nickle":0.05,
       "dime":0.10,
       "quarter":0.25
       }

money_in_machine=0


def check_requirements(requirement,already_present):
    c=0
    if not requirement["water"]<already_present["water"]:
        c+=1
        print("\nwater is insufficient")
    if not requirement["milk"]<already_present["milk"]:
        c+=1
        print("\nmilk is insufficient")
    if not requirement["coffee"]<already_present["coffee"]:
        c+=1
        print("\ncoffee is insufficient")
         
    global resources
    resources["water"]-=requirement["water"]
    resources["milk"]-=requirement["milk"]
    resources["coffee"]-=requirement["coffee"]
            
    if c!=0 :
        print(resources)
        return False
    else:

        return True
    
def check_amount_paid(amount):
    global money_in_machine
    print(f"amount to be paid is : ${amount}")
    amount=float(amount)
    no_of_penny=int(input("enter no. of pennies deposited : "))
    no_of_nickle=int(input("enter no. of nickle deposited : "))
    no_of_dime=int(input("enter no. of dime deposited : "))
    no_of_quarter=int(input("enter no. of quarter deposited : "))
    inputed_amount=(no_of_penny*0.01)+(no_of_nickle*0.05)+(no_of_dime*0.10)+(no_of_quarter*0.25)
    money_in_machine+=inputed_amount
    if(inputed_amount>=amount):
        return True
    else:
        print("\n\n")
        shortage=amount-inputed_amount
        print(f"you are ${shortage} less\n\n")
        decision=input(f"press y to add the shortage amount of {shortage}\n\nElse press n to take back your money: ")
        if (decision=="y"):
            print(f"amount to be paid is : ${shortage}")
            no_of_penny=int(input("enter no. of pennies deposited : "))
            no_of_nickle=int(input("enter no. of nickle deposited : "))
            no_of_dime=int(input("enter no. of dime deposited : "))
            no_of_quarter=int(input("enter no. of quarter deposited : "))
            inputed_amount=(no_of_penny*0.01)+(no_of_nickle*0.05)+(no_of_dime*0.10)+(no_of_quarter*0.25)
            money_in_machine+=inputed_amount
            if(inputed_amount>=shortage):
                return True
            
        else:
            return False

def coffee(name_of_coffee):
    user_input=menu[name_of_coffee]
    ingredients_required=user_input["ingredients"]
    cost=user_input["cost"]
    if(check_requirements(ingredients_required,resources)==True):
        if(check_amount_paid(cost)==True):
            print(f"\n\nHERE IS YOUR {name_of_coffee}, THANKS AND VISIT AGAIN")
        else:
            print("you were not able to pay the required amount so here's the amount you paid\n\n")
    else:
        print("sry we do not have enough resources")

machine_is_off=False
while(machine_is_off==False):
    print("\n\nHELLO CUSTOMER \n")
    choice_of_coffee_made=input("""MENU IS,
             espresso
             latte
             cappuccino
             
             : """)
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
        coffee(choice_of_coffee_made)  