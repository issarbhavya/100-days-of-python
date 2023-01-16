from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from halfline import Half_line
import time
game_is_on=True
win_points=2



screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("purple")


l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
ball.speed(5)
score=Scoreboard()
half_line=Half_line()

def end_game():
    global game_is_on
    game_is_on=False
    score.game_ends()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"e")
screen.onkey(l_paddle.go_down,"d")



r_score_count=0
l_score_count=0
while(game_is_on==True):
    time.sleep(ball.ball_speed)
    screen.update()
    if(ball.xcor()>380):
        score.left_scored()
        ball.goto(0,0) 
        ball.x_flip()
        l_score_count +=1
        ball.ball_speed = 0.06

        
    if(ball.xcor()< -380):
        score.right_scored()
        ball.goto(0,0) 
        ball.x_flip()
        r_score_count +=1
        ball.ball_speed = 0.06
                
    if(ball.xcor()> 330 or ball.xcor()< -330):
        if(ball.distance(r_paddle)<50):
            ball.x_flip()
            ball.ball_speed *= 0.9
            
        if(ball.distance(l_paddle)<50):
            ball.x_flip()
            ball.ball_speed *= 0.9
          
            
    ball.move()
    if(r_score_count>win_points or l_score_count>win_points):
        end_game()
        

    
screen.exitonclick()