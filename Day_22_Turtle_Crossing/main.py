import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkeypress(key="Up", fun=player.move)


game_is_on = True
nr_game_loop = 0
while game_is_on:
    time.sleep(0.1)
    nr_game_loop += 1
    if nr_game_loop == 6:
        car_manager.generate_car()
        nr_game_loop = 0
    car_manager.move_cars()
    screen.update()
    if player.ycor() >= 280:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_speed()
    for car in car_manager.cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False
            car_manager.should_generate = False
        if car.xcor() < -320:
            car_manager.remove_car(car)



















screen.exitonclick()