from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

display = Screen()
display.setup(width=600, height=600)
display.bgcolor("black")
display.title("snake game")
display.tracer(0)

snake = Snake()
food = Food()
player_score = ScoreBoard()

display.listen()
display.onkey(snake.up, "Up")
display.onkey(snake.down, "Down")
display.onkey(snake.right, "Right")
display.onkey(snake.left, "Left")

game_on = True
while game_on:
    display.update()
    time.sleep(0.1)
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        player_score.increase_score()

    # Detecting collision with the wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        player_score.reset()
        snake.reset()
    # Detect collision with tail
    for segment in snake.segments[2:]:
        # If head collides with any segment in the tail
        if snake.head.distance(segment) < 15:
            # trigger the game over
            player_score.reset()

display.exitonclick()
