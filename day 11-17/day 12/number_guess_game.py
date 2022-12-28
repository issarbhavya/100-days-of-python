import random
print("welcome to the number guessing game !!!")
num=random.randint(0,100)

game=""
while(game!="E" and game!="H"):
    game=input("enter E for easy nd H for hard : ")
    if(game=="E"):
        lives=10
    elif(game=="H"):
        lives= 6
    else:
        print("wrong selection, select again \n")

print(f"the computer has already choosen a number between 1 to 100 and you have {lives} lives to guess it")     
choice=0
while(choice!=num and lives!=0):
    choice=int(input("\nenter your guess : "))
    if(choice>num):
        print("your choice is HIGHER then the no.")
    elif(choice<num):
        print("your choice is LOWER than the no.")
    lives=lives-1
    print(f"no. of lives left : {lives}\n")
    
if(choice==num):
    print("YOU WON !!!!\n")
    print(f"the no. was {num}")
    print(f"you still had {lives} lives left")
else:
    print("lives over... YOU LOOSE !!!")
    print(f"the no. was {num}")