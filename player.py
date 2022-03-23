from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    # Initial parameters
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setpos(STARTING_POSITION)
        self.setheading(90)
    
    # Handling the movement
    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    # Reseting a position of the player
    def reset_pos(self):
        self.setpos(STARTING_POSITION)
