from turtle import Screen
from paddel import Paddeline
from ball import SPEED_BALL, Ball
from scoreboard import Scoreboard

# screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

# paddel
paddel = Paddeline(x_y=(350, 0))
paddel_2 = Paddeline(x_y=(-350, 0))

# score
scoreboar = Scoreboard()
# ball
ball = Ball((0, 0))

# detectar eventos
screen.onkeypress(paddel_2.up, 'e')
screen.onkeypress(paddel_2.down, 'd')
screen.onkeypress(paddel.up, 'Up')
screen.onkeypress(paddel.down, 'Down')
screen.listen()


game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    # detect colision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision whit paddel
    if ball.distance(paddel) < 50 and ball.xcor() > 340 or ball.distance(paddel_2) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        SPEED_BALL += 0.1
        print(SPEED_BALL)

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboar.l_point()
        SPEED_BALL = 0.5

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboar.r_point()
        SPEED_BALL = 0.5

screen.exitonclick()
