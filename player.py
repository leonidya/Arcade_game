from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def move(self):
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(0, y_cor)
        # if self.ycor()
