from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 4

class CarManager(Turtle):
    
    # Initial parameters
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.move_speed = 6

    # Creating a car
    def createCar(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.pu()
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setpos(300, random.randint(-230, 260))
        self.cars.append(car)

    # Moving all the cars
    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_speed)

    # Increasing a speed of cars
    def next_level(self):
        self.move_speed += MOVE_INCREMENT