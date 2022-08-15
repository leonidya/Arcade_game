from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreborad()

    def update_scoreborad(self):
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_scoreborad()

    def game_over(self):
        self.goto(-80, 0)
        self.write("GAME OVER", font=FONT)

