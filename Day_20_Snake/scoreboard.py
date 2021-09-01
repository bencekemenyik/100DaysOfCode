from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.pencolor("DarkOrchid2")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.write_text()

    def write_text(self):
        self.clear()
        self.write(f"Score: {self.current_score} High score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("high_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.write_text()


    def add_point(self):
        self.current_score += 1
        self.write_text()
