from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((380, 0))
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

l_paddle = Paddle((-380, 0))
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
scoreboard = ScoreBoard()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 287 or ball.ycor() < -287:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 360 or ball.distance(l_paddle) < 60 and ball.xcor() < -360:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_pos()
        ball.bounce_x()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_pos()
        ball.bounce_x()
        scoreboard.r_point()

screen.exitonclick()
