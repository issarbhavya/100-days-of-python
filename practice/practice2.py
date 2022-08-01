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
                if ingredients[items]<resources[items]:
                      c+=1
                else:
                  print(f"{items} is not suffecient for{order}")
          if(c==3):
                avaliable_items.append(order)
    return avaliable_items

avaliable_in_menu()