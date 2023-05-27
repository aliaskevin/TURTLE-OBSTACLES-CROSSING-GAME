from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = 0
        self.add_score()

    def add_score(self):
        self.clear()
        self.goto(-210, 260)
        self.write(f"SCORE: {self.score}", move=False, align="center", font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)
