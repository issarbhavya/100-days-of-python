import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice="y"
while(choice=="y"):
    
    user_choice= int(input("enter 1 for rock, 2 for paper,3 for scissor "))
    computer_choice= random.randint(1,3)
    for_print=[scissors,rock,paper,scissors,rock]
    print("USER : ")
    print(for_print[user_choice])
    print("computer : ")
    print(for_print[computer_choice])
    
    if(user_choice==computer_choice):
        print("tie")
    elif(user_choice==computer_choice-1 or user_choice==computer_choice+2):
        print("computer won, sryyyyy !!!!")
    elif(user_choice==computer_choice+1 or user_choice==computer_choice-2):
        print("you won")
        
    choice=input("enter y to cntinue playing :")        
print ("\nThanks for playing")