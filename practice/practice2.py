from turtle import Turtle,Screen
screen=Screen()
screen.setup(height=400, width=500)
user_bet=screen.textinput(title="make your bet :-",  prompt="choose turtle you want to bet on : ")

colors=["red","green","yellow","blue","purple"]
l=len(colors)

p_red=Turtle()
p_green=Turtle()
p_yellow=Turtle()
p_blue=Turtle()
p_purple=Turtle()

players_list=[p_red,p_green,p_yellow,p_blue,p_purple]
y=-100
for i in range(0,l):
    players_list[i].color(colors[i])
    players_list[i].shape("turtle")
    players_list[i].speed(10)
    players_list[i].penup()
    players_list[i].goto(-240,y)
    players_list[i].pendown()
    players_list[i].speed("normal")
    y=y+50



    
    
    
    
    
    
    
    
    
screen.exitonclick()