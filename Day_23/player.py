from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270

class Player(Turtle):
    def __init__(self, shape="turtle"):
        super().__init__(shape)
        self.left(90)
        self.penup()
        self.restart_turtle()

    def go_up(self):
        self.forward(MOVE_DISTANCE)   

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            False

    def restart_turtle(self):
        self.goto(STARTING_POSITION)

