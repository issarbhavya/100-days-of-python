from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()
def move_fd():
    timmy.fd(50)
def move_back():
    timmy.backward(50)
def turn_right():
    timmy.right(10)
def turn_left():
    timmy.left(10) 
def clean():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(move_fd,"w")
screen.onkey(move_back,"s")
screen.onkey(turn_right,"d")
screen.onkey(turn_left,"a")
screen.onkey(clean,"c")

screen.exitonclick()

