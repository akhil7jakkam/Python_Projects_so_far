from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=450)
user_bet = screen.textinput(title="Make your bet", prompt="Which colour turtle will win the race?").lower()

colors = ["red", "orange", "magenta", "green", "blue", "purple"]
x = -220
y = -170
race_on = False
turtles = []

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 70
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 215:
            won_color = turtle.pencolor()
            if user_bet == won_color:
                print(f"You have won! The {won_color} turtle is the winner!")
            else:
                print(f"You lost! The {won_color} turtle is the winner!")
            race_on = False
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
