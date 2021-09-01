import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for color in colors:
    new_turtle = t.Turtle("turtle")
    new_turtle.color(color)
    turtles.append(new_turtle)

LEFT_END_OF_SCREEN = -230
RIGHT_END_OF_SCREEN = 250
start_y = 125
for turtle in turtles:
    turtle.penup()
    turtle.goto(x=LEFT_END_OF_SCREEN, y=start_y)
    start_y -= 50

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.fillcolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





screen.exitonclick()