import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize objects
player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

# Handling controls
screen.listen()
screen.onkey(player.move_forward, "Up")

# The main game logic
game_is_on = True
while game_is_on:
    # Update screen diplay after a delay
    time.sleep(0.1)
    screen.update()
    
    # Move all the cars
    carManager.move_cars()

    # Randomly create a car
    if random.randint(0, 5) == 0:
        carManager.createCar()

    # Detect a collision of player and a car
    for car in carManager.cars:
        if player.distance(car) < 21:
            game_is_on = False
            scoreboard.gameover()

    # Detecting if a player has reached the finish line
    if player.ycor() >= 290:
        carManager.next_level()
        player.reset_pos()
        scoreboard.increase_score()
        scoreboard.display_score()

screen.exitonclick()