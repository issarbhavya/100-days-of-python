from turtle import Turtle



class Half_line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(10)
        self.pencolor("black")
        self.hideturtle()
        self.goto(0,-300)
        self.left(90)
        c=1
        while(self.ycor()<300):
            if(c%2==0):
                self.penup()
            else:
                self.pendown()
            c +=1
            self.fd(50)