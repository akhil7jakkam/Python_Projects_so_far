import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
tim.speed(0)
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


for _ in range(72):
    tim.circle(100)
    tim.left(5)
    tim.color(random_colour())

screen.exitonclick()
