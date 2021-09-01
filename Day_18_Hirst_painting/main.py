import colorgram
from turtle import Turtle
from turtle import Screen
from turtle import colormode
import random

# colors = colorgram.extract("yes.jpg", 30)
# list_of_colors = []
# for color in colors:
#     rgb = (color.rgb[0], color.rgb[1], color.rgb[2])
#     list_of_colors.append(rgb)
# print(list_of_colors)

random_colors = [(243, 235, 74), (211, 158, 93), (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31)]

timmy = Turtle()
timmy.speed(0)
timmy.hideturtle()
colormode(255)
start_x = -250
start_y = -250
timmy.penup()
timmy.setx(-250)
timmy.sety(-250)
for _ in range(10):
    timmy.setx(start_x)
    timmy.sety(start_y + (_ * 50))
    for __ in range(10):
        timmy.setx(start_x + (__ * 50))
        timmy.dot(20, random.choice(random_colors))












screen = Screen()
screen.exitonclick()