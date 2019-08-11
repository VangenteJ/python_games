from random import *
from turtle import *
from base import Vector
turtle = Turtle()
screen = Screen()

ant = Vector(0, 0)
aim = Vector(2, 0)

def wrap(value):
    return value

def draw():
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)
    aim.move(random() - 0.5)

    aim.rotate(random() * 10 - 5)
    turtle.clear()

    turtle.goto(ant.x, ant.y)
    turtle.dot(4)

    if turtle.running:
        screen.ontimer(draw, 100)

screen.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle._tracer(False)
turtle.up()
turtle.running = True
draw()
done()


