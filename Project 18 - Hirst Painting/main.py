import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
rgb_colors = [(66, 93, 145), (215, 155, 95), (146, 73, 55), (235, 204, 121), (152, 74, 96), (77, 160, 102), (228, 74, 49), (53, 132, 98), (135, 163, 200), (138, 190, 159), (206, 84, 106), (208, 124, 143), (155, 209, 190), (50, 41, 75), (62, 54, 102), (116, 100, 164), (83, 53, 60), (161, 196, 226), (156, 200, 223), (221, 174, 183), (64, 45, 51), (56, 56, 51), (227, 175, 168), (66, 68, 56), (72, 149, 154), (107, 48, 44), (149, 139, 89), (24, 75, 96), (56, 58, 55)]

timmy.speed("fastest")
timmy.penup()
timmy.setheading(225)
timmy.forward(290)
timmy.setheading(0)
timmy.back(20)

for i in range(10):
    initial_y = timmy.ycor()
    initial_x = timmy.xcor()
    for i in range(10):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.penup()
        timmy.forward(50)
    timmy.setx(initial_x)
    timmy.sety(initial_y + 50)













screen = Screen()
screen.exitonclick()
