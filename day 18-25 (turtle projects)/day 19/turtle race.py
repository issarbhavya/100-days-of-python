from turtle import Turtle,Screen
import random

screen=Screen()

game_on=False
screen.setup(height=400, width=500)
user_bet=screen.textinput(title="make your bet :-",  prompt="choose your bet <<  red,green,yellow,blue or purple turtle :- ")

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
end_line_turtle.pensize(10)
end_line_turtle.hideturtle()
end_line_turtle.penup()
end_line_turtle.goto(220,-300)
end_line_turtle.pendown()
end_line_turtle.goto(220,300)

if user_bet:
    game_on=True
    
while(game_on==True):
    for i in all_turtle:
        speed=random.randint(0,10)
        i.fd(speed)
       # end=i.xcor()
        if(i.xcor() >= 210):
            winner=colors[all_turtle.index(i)]
            if(user_bet==winner):
                print(f"\n\nrace ended, you'r bet was correct, {winner} WON !!!")
            else:
                print(f"\n\nrace ended, your choice was << {user_bet} >> but, {winner} won ")
            game_on=False
            break
    
screen.exitonclick()