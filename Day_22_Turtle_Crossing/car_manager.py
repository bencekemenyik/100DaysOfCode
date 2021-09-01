from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Turtle("square")
        new_car.setheading(180)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(x=300, y=random.randint(-250,280))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def remove_car(self, car):
        self.cars.remove(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT



