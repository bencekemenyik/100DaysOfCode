from turtle import Turtle
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLOR = "white"
FONT = ("Arial", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.penup()
        self.hideturtle()
        self.pencolor(COLOR)

        self.write_text()


    def write_text(self):
        self.clear()
        self.goto(x=-100, y=SCREEN_HEIGHT / 2 - 130)
        self.write(f"{self.player1_score}", align="center", font=FONT)
        self.goto(x=100, y=SCREEN_HEIGHT / 2 - 130)
        self.write(f"{self.player2_score}", align="center", font=FONT)

    def increase_player_point(self, player):
        if player == "player1":
            self.player1_score += 1
            self.write_text()
        else:
            self.player2_score += 1
            self.write_text()





