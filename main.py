import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

STARTING_POSITION = (0, -280)

TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
game_is_on = True

while game_is_on:
    time.sleep(TIME)
    screen.update()
    screen.onkey(player.move, key="Up")
    if player.ycor() > 280:
        player.goto(STARTING_POSITION)
        TIME *= 0.9
        scoreboard.level_up()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()