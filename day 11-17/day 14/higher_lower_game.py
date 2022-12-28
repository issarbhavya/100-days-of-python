from art import logo
from art import vs
print(logo)
from game_data import data

def show(a,b):
    name=a["name"]
    description=a["description"]
    country=a["country"]
    print(f"a : {name} is {description} who lives in {country}")
    print(vs)
    name=b["name"]
    description=b["description"]
    country=b["country"]
    print(f"b : {name} is {description} who lives in {country}\n\n")


print("guess who has the highest followers out of the two")

#randomly choose a and b
import random
answer=True
score=0

a=random.choice(data)
data.remove(a)
b=random.choice(data)
data.remove(b)


while(answer==True):
    
    show(a,b)  
    your_choice=input("enter who has the highest followers(in million) \na or b : ")
    print("\n\n")
    a_followers=a["follower_count"]
    b_followers=b["follower_count"]
    
    if(your_choice=="a"):
        if(a_followers > b_followers):
              score=score+1
              print(f"score : {score}\nRound {score+1}\n")
              a=b
              b=random.choice(data)
              data.remove(b)
        elif(a_followers < b_followers):
              print("you loose !!!")
              print(f"a has {a_followers}M followers whereas b has {b_followers}M followers")
              answer=False
              
    if(your_choice=="b"):
        if(a_followers < b_followers):
              score=score+1
              print(f"score : {score}\nRound {score+1}\n")
              a=b
              b=random.choice(data)
              data.remove(b)
        elif(a_followers > b_followers):
              print("you loose !!!")
              print(f"a has {a_followers}M followers whereas b has {b_followers}M followers")
              answer=False
              