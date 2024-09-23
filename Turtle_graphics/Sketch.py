import turtle as t

tim = t.Turtle()
screen = t.Screen()

screen.listen()


def go():
    tim.forward(10)


def back():
    tim.back(10)


def left():
    tim.left(5)


def right():
    tim.right(5)


screen.onkey(key="w", fun=go)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=screen.resetscreen)

screen.exitonclick()
