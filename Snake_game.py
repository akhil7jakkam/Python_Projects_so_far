from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer()

segments = []
x = 0
y = 0
for n in range(3):
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.speed(0)
    segment.goto(x, y)
    x -= 20
    segments.append(segment)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)

screen.exitonclick()
