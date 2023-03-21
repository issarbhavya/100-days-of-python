from turtle import Turtle



class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        
        self.x_value=10
        self.y_value=10
        self.ball_speed= 0.06
       
        
    def move(self):
        new_x=self.xcor() + self.x_value
        new_y=self.ycor() + self.y_value
        if(self.ycor() == 280 ):
            self.y_value= -10
        if(self.ycor()== -280):
            self.y_value= 10
        self.goto(new_x,new_y)
        
        
    def x_flip(self):
        self.x_value *= -1

