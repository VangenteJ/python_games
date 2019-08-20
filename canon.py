from random import *
from turtle import *
from base import Vector

ball = Vector(-200, -200)
speed = Vector(0, 0)
targets = []

def inside(x_y):
    return -200 < x_y.x < 200 and -200 < x_y.y < 200

def tap(x, y):
    # Launch the ball when the screen is tapped 
    # Only one ball at time
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 5
        speed.y = (y + 200) / 25
    
def draw():
    # Draw balls and targets
    clear()
    for target in targets:
        goto(target.x, target.y)
        dot(20, "Blue")
    
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, "Red")

    update()

def move():
    # Mov of the ball and target

    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = Vector(200, y)
        targets.append(target)
    
    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    
    duplicate = targets.copy()
    targets.clear()

    for target in duplicate:
        if abs(target - ball) > 13:
            targets.append(target)
    
    draw()

    for target in targets:
        if not inside(target):
            return
    
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()




