from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.goto(x=-200, y=250)
        self.level = 1
        self.write_text()

    def write_text(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_text()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", align="center", font=FONT)
