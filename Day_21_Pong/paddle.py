from turtle import Turtle

COLOR = "white"

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(COLOR)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

