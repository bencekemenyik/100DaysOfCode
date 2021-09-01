from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()

scoreboard = Scoreboard()
left_position = (-1 * (SCREEN_WIDTH / 2 - 50), 0)
right_position = (SCREEN_WIDTH / 2 - 50, 0)
left_paddle = Paddle(left_position)
right_paddle = Paddle(right_position)

ball = Ball()


screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
speed = 0.05
game_over = False
while game_over is False:
    ball.move()
    screen.update()
    time.sleep(speed)

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 330:
        if ball.distance(right_paddle) < 50:
            ball.deflect()
            speed *= 0.95
        else:
            ball.reset_position()
            scoreboard.increase_player_point("player1")
            speed = 0.05
    elif ball.xcor() < -330:
        if ball.distance(left_paddle) < 50:
            ball.deflect()
            speed *= 0.95
        else:
            ball.reset_position()
            scoreboard.increase_player_point("player2")
            speed = 0.05










































screen.exitonclick()
