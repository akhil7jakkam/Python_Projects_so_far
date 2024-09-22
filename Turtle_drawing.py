import turtle as t
pen = t.Turtle()
screen = t.Screen()


def forward():
    pen.forward(10)


def backward():
    pen.backward(10)


def right():
    pen.right(5)


def left():
    pen.left(5)


def clear():
    screen.reset()


screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='a', fun=left)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
