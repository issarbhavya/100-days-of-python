from turtle import Turtle , Screen
import random
timmy=Turtle()
l = ["red","green","blue","yellow",]

def draw_row(n):
    global l
    for i in range (0,n):
        colour=random.choice(l)
        timmy.dot(10,colour)
        timmy.fd(10)
    
    
    
timmy.penup()
timmy.setpos(-200,-200)
y=-200
timmy.shape("turtle")
for i in range(0,10):
    draw_row(50)
    y=y+10
    timmy.setpos(-200,y)



screen=Screen()
screen.exitonclick()