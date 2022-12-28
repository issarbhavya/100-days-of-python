from turtle import Turtle,Screen
import random

screen=Screen()

game_on=False
screen.setup(height=400, width=500)
user_bet=screen.textinput(title="make your bet :-",  prompt="choose turtle you want to bet on : ")

y=-100
colors=["red","green","yellow","blue","purple"]
all_turtle=[]
for i in range(0,5):
    s=colors[i]
    s=Turtle(shape="turtle")
    s.color(colors[i])
    s.speed(10)
    s.penup()
    s.goto(-240,y)
    s.penup
    s.speed(6)
    all_turtle.append(s)
    
    y=y+50

end_line_turtle=Turtle()
end_line_turtle.pensize(5)
end_line_turtle.hideturtle()
end_line_turtle.penup()
end_line_turtle.goto(230,-300)
end_line_turtle.pendown()
end_line_turtle.goto(230,300)

if user_bet:
    game_on=True
    
while(game_on==True):
    for i in all_turtle:
        speed=random.randint(0,10)
        i.fd(speed)
       # end=i.xcor()
        if(i.xcor() >= 220):
            if(user_bet==i):
                print(f"\n\nrace ended, you'r bet was correct, {i} WON !!!")
            else:
                print(f"\n\nrace ended, {user_bet} turtle you had bet on LOST, {i} won ")
            game_on=False
            break
    
screen.exitonclick()