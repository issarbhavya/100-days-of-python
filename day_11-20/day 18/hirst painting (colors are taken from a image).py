import colorgram
from turtle import Turtle , Screen
import random
timmy=Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()

def draw_row(n):
    global l
    for i in range (0,n):
        colour=choose_color()
        timmy.dot(10,colour)
        timmy.fd(10)   

timmy.setpos(-200,-200)
y=timmy.ycor()
timmy.shape("turtle")
for i in range(0,10):
    draw_row(30)
    y=y+10
    timmy.setpos(-200,y)






screen=Screen()
screen.exitonclick()
