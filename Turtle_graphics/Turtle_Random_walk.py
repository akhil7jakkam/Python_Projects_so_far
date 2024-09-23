from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

tim.speed(0)
tim.pensize(10)
directions = [0, 45, 90, 135, 180, 225, 270, 315]
while True:
    way = [tim.right(random.choice(directions)), tim.left(random.choice(directions))]
    num1 = random.randint(1, 255)
    num2 = random.randint(1, 255)
    num3 = random.randint(1, 255)
    screen.colormode(255)
    tim.color(num1, num2, num3)
    tim.forward(30)
    random.choice(way)

# screen.exitonclick()
