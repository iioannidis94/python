import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
screen.listen()
screen.onkey(player.up, "Up")
scoreboard.update_scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect the collision
    for car in car_manager.all_cars:
        if car.distance(player) < 28:
            scoreboard.game_over()
            game_is_on = False

    # detect crossing
    if player.is_at_finish_line():
        player.refresh()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
