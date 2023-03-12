import turtle
from random import randint

turtle.screensize(250, 250)
turtle.colormode(255)
tim = turtle.Turtle()

#Draw Bounds:
tim.penup()
tim.goto(250, 250)
tim.pendown()
for t in range(4):
    tim.right(90)
    tim.forward(500)
    print(tim.pos())
tim.penup()
tim.goto(0,0)
tim.pendown()
tim.pensize(10)
tim.speed(1000)
# #task 1: Draw a Square
#
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# turtle.exitonclick()

# #Task 2: Shapes
# sides = 11
# while sides >= 3:
#     tim.pencolor(randint(1, 255),
#                  randint(1, 255),
#                  randint(1, 255))
#     for i in range(sides):
#         tim.begin_fill()
#         tim.forward(75)
#         tim.right(360/sides)
#         tim.end_fill()
#     sides -= 1

def direction():
    num = randint(0, 2)
    pos = tim.pos()
    xMin = -250
    xMax = 250
    yMin = -250
    yMax = 250
    if num == 0:
        if xMin - int(pos[0]) > -21:
            print("Left Edge Detected")
            tim.seth(0)
        elif xMax - int(pos[0]) < 21:
            print("Right Edge Detected")
            tim.seth(180)
        elif yMin - int(pos[1]) > -21:
            print("Bottom Edge Detected")
            tim.seth(90)
        elif yMax - int(pos[1]) < 21:
            print("Top Edge Detected")
            tim.seth(270)
        tim.forward(20)
    elif num == 1:
        tim.left(90)
    elif num == 2:
        tim.right(90)

while (True):
    tim.pencolor(randint(1, 255),
                 randint(1, 255),
                 randint(1, 255))
    direction()





turtle.exitonclick()