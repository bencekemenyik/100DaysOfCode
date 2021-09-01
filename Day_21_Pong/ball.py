from turtle import Turtle

COLOR = "white"

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(COLOR)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x_pos = self.xcor() + self.x_move
        new_y_pos = self.ycor() + self.y_move
        self.goto(new_x_pos, new_y_pos)

    def bounce(self):
        self.y_move *= -1

    def deflect(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.deflect()

