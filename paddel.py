from turtle import Turtle


SPEED = 20


class Paddeline(Turtle):
    def __init__(self,  x_y):
        super().__init__()
        self.goto(x_y)
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.sety(self.ycor() + SPEED)

    def down(self):
        self.sety(self.ycor() - SPEED)
