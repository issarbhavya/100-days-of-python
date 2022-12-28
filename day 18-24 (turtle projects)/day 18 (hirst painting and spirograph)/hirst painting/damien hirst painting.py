import turtle
turtle.colormode(255)
from turtle import Turtle , Screen
import random
timmy=Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()
def choose_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    col=(r,g,b)
    return col

def draw_row(n):
    global l
    for i in range (0,n):
        colour=choose_color()
        timmy.dot(20,colour)
        timmy.fd(50)   

timmy.setpos(-200,-200)
y=timmy.ycor()
timmy.shape("turtle")
for i in range(0,10):
    draw_row(10)
    y=y+50
    timmy.setpos(-200,y)



screen=Screen()
screen.exitonclick()









