from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.up()
        self.down()

    def up(self):
        new_y = self.ycor()+30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor()-30
        self.goto(self.xcor(), new_y)
