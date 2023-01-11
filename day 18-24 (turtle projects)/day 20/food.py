from turtle import Turtle,Screen
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        x=random.randint(-280,280)   
        y=random.randint(-280,280)
        self.goto(x,y)   
# t=Food()
# t.refresh()
# screen=Screen()
# screen.exitonclick()
