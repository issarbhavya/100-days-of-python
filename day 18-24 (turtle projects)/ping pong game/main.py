from turtle import Screen,Turtle
from paddle import Paddle

screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("red")



l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True

while(game_is_on==True):
    screen.update()

    
    
    
    
    
screen.exitonclick()