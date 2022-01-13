from turtle import Turtle
SPEED_BALL = 0.5

class Ball(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(pos)
        self.x_move = SPEED_BALL
        self.y_move = SPEED_BALL

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()