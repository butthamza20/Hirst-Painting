import random
from turtle import Turtle, Screen
import turtle

tim = Turtle()
tim.shape("circle")
turtle.colormode(255)
tim.speed(0)
tim.hideturtle()

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
              (224, 141, 211), (10, 97, 61)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dots in range(1, num_of_dots + 1):
    tim.dot(len(color_list), random.choice(color_list))
    tim.forward(50)
    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
