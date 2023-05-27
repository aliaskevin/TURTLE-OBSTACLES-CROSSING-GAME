
from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SIDE = [-1, 1]


class CarManager:
    def __init__(self):
        self.move_dist = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.initialize_car()
        self.x_cord = None
        self.direction = None
        self.final_x_cord = None

    def initialize_car(self):
        for num in range(20):
            self.x_cord = randint(20, 270)
            self.direction = choice(SIDE)
            self.final_x_cord = self.x_cord * self.direction
            self.new_cars()

    def more_cars(self):
        self.final_x_cord = randint(270, 300)
        self.new_cars()

    def new_cars(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.setheading(180)
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(choice(COLORS))
        y_cord = randint(50, 250)
        self.direction = choice(SIDE)
        final_y_cord = y_cord * self.direction
        car.setposition(self.final_x_cord, final_y_cord)
        self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_dist)

    def speed_up(self):
        self.move_dist += MOVE_INCREMENT

