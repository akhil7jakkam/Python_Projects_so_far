import turtle as t
import random

t.colormode(255)
my_turtle = t.Turtle()
my_turtle.speed(0)
direction = 0


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r, g, b)
    return colour_tuple


for _ in range(73):
    my_turtle.color(random_colour())
    my_turtle.circle(150)
    my_turtle.setheading(direction)
    direction += 5

my_screen = t.Screen()
my_screen.exitonclick()
