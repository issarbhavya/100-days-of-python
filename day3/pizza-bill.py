print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza_cost=0
pepperoni=0
cheese_cost=0

if(size=="S"):
    pizza_cost=15
    if(add_pepperoni== "y"):
        pepperoni=2
total=pizza_cost+pepperoni+cheese_cost       
if(size=="M"):
    pizza_cost=20
    if(add_pepperoni== "y"):
        pepperoni=3
    else :
        pepperoni=0
if(size=="L"):
    pizza_cost=25
    if(add_pepperoni== "y"):
        pepperoni=3
    else :
        pepperoni=0
if(extra_cheese=="y"):
    cheese_cost=1
else:
    cheese_cost=0
    
total=pizza_cost+pepperoni+cheese_cost
print(f"Your final bill is: ${total}")
