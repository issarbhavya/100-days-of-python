from turtle import Turtle , Screen
import random
timmy=Turtle()
def row_up_from_right():
    timmy.left(90)
    timmy.fd(20)
    timmy.left(90)
def row_up_from_left():
    timmy.right(90)
    timmy.fd(20)
    timmy.right(90)
    
timmy.penup()
timmy.setpos(-300,-300)
timmy.shape("circle")
l=["red","green","blue","yellow",]


while (timmy.pos()<=300,300):
    colour=random.choice(l)
    timmy.dot(20,colour)
    timmy.fd(20)
    if(timmy.xcor()==300):
        row_up_from_right()
    if(timmy.xcor()==-300):
        row_up_from_left()
    screen=Screen()
    screen.exitonclick()










