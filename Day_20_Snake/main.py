from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if food.distance(snake.head_of_the_snake) < 15:
        scoreboard.add_point()
        food.change_location()
        snake.extend()

    # Detect collision with wall
    if snake.head_of_the_snake.xcor() > 280 or snake.head_of_the_snake.xcor() < -280 or snake.head_of_the_snake.ycor() > 280 or snake.head_of_the_snake.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head_of_the_snake.distance(segment) < 10:
            scoreboard.reset()

    # if head collides with any segment in the tail:
        # trigger game_over































screen.exitonclick()
