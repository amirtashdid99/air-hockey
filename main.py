from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("pong")
screen.tracer(0)

paddle1 = Paddle()
paddle1.color('blue')
paddle2 = Paddle()
paddle2.color('red')
ball = Ball()
scoreboard = Scoreboard()



paddle1.goto(350, 0)
paddle2.goto(-350, 0)

screen.listen()
screen.onkey(paddle1.paddle_up, "Up")
screen.onkey(paddle1.paddle_down, "Down")
screen.onkey(paddle2.paddle_up, "w")
screen.onkey(paddle2.paddle_down, "s")

while True:
    spe=ball.move_speed
    time.sleep(spe)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 325 or ball.distance(paddle2)<50 and ball.xcor() < -325 :

        ball.bounce_x()

    if ball.xcor() > 360 :
        scoreboard.lp()
        ball.reset()

    if ball.xcor() < -360 :
        scoreboard.rp()
        ball.reset()




screen.exitonclick()
