import random

lst=[]
player=[]
player_display=[]
computer=[]
computer_display=[]
computer_display_full=[]
base=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]



def choose(card):
    if(card=="J" or card=="Q" or card=="K"):
        card=10
    elif(card=="A"):
        card=11
    return card
      
def add_cards(lst):
    card=random.choice(base)
    lst.append(card)
    return lst

def check(player_sum,computer_sum):
    if(player_sum>21):
        return "\n\nYOU LOOSE  !!!"

    elif(player_sum>computer_sum):
        return "\n\nYOU WON !!!"
    
    elif(player_sum==computer_sum):
        return "\n\nDRAW"
        
    else:
        return "\n\nYOU LOOSE !!!"

#for player
player_display=add_cards(player_display)
player_display=add_cards(player_display)

print(player_display)

player_sum=0
for i in player_display:
    i=choose(i)
    player_sum = player_sum + i 


#for computer
computer_display=add_cards(computer_display)
computer_display=add_cards(computer_display)

computer_display_full=computer_display.copy()

computer_sum=0
for i in computer_display:
    i=choose(i)
    computer_sum= computer_sum + i

computer_display[1]="*"
print(computer_display)


condition=input("enter yes to draw 3rd card else\nPress r for result : ")
print("\n\n")

if(condition=="yes"):
    
    player_display=add_cards(player_display)
    i=player_display[2]
    i=choose(i)
    player_sum+=i
    print(f"player ={player_display}")
    print(f"computer ={computer_display_full}")
    print(check(player_sum,computer_sum))
          
elif(condition=="r"):
    print(f"player ={player_display}")
    print(f"computer ={computer_display_full}")
    print(check(player_sum,computer_sum))
    
else:
    print("wrong selection")




    


    
