import turtle
turtle.colormode(255)
from turtle import * 
import random

timmy=Turtle()
timmy.speed(10)
timmy.pensize(3)

def choose_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    col=(r,g,b)
    return col

for i in range (0,36):
    timmy.color(choose_color())
    timmy.circle(100)
    timmy.left(10)
    
screen=Screen()
screen.exitonclick()







