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

user_choice= int(input("enter 0 for rock, 1 for paper,2 for scissor "))
computer_choice= random.randint(0,2)
for_print=[rock,paper,scissors]
print(for_print[user_choice])
print(for_print[computer_choice])

if (user_choice>2 or user_choice<0):
      print ("invalid input")
      
if user_choice==0:
      if computer_choice==0:
            print("tie")
      elif computer_choice==1:
            print("you losse")
      elif computer_choice==2:
            print("you win")

if user_choice==1:
      if computer_choice==0:
            print("you win")
      elif computer_choice==1:
            print("tie")
      elif computer_choice==2:
            print("you loose")     
            
if user_choice==2:
      if computer_choice==0:
            print("you loose")
      elif computer_choice==1:
            print("you win")
      elif computer_choice==2:
            print("tie")