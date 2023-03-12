import turtle
from random import randint

turtle.colormode(255)
tim = turtle.Turtle()
# #task 1: Draw a Square
#
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# turtle.exitonclick()

tim.pensize(5)
sides = 11
while sides >= 3:
    tim.pencolor(randint(1, 255),
                 randint(1, 255),
                 randint(1, 255))
    for i in range(sides):
        tim.begin_fill()
        tim.forward(75)
        tim.right(360/sides)
        tim.end_fill()
    sides -= 1

turtle.exitonclick()