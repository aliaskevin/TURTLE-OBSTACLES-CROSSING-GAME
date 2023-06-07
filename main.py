import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# Initializing the player and environment
loop_time = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
# Listening to Up arrow key strokes
screen.listen()
screen.onkey(player.up, "Up")
# main loop of game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()
    if player.finish():
        player.reset_player()
        car_manager.speed_up()
        scoreboard.add_score()
    if loop_time > 6:
        car_manager.more_cars()
        loop_time = 0
    loop_time += 1
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
