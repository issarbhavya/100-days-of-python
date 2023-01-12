from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.penup()
        self.hideturtle()
        self.update()
        
        
        
    def left_scored(self):
        self.l_score +=1
        self.update()
        
    def right_scored(self):
        self.r_score +=1
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("couries", 80 , "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("couries", 80 , "normal"))
        
    def game_ends(self):
        
        self.goto(0,0)
        self.pencolor("white")
        if(self.l_score>self.r_score):
            self.write("Left player wins !!!" , align="center", font=("couries", 60 , "normal"))
        else:
            self.write("Right player wins !!!", align="center", font=("couries", 60 , "normal"))
        
        
