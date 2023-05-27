from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_player()
    
    def reset_player(self):
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reset_player()
            return True
        else:
            return False

