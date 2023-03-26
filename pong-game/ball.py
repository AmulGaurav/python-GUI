from turtle import Turtle

MOVE_DISTANCE_X = 3
MOVE_DISTANCE_Y = 3


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.02
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=0)

    def move(self):
        new_x = self.xcor() + MOVE_DISTANCE_X
        new_y = self.ycor() + MOVE_DISTANCE_Y
        self.goto(new_x, new_y)

    def bounce_y(self):
        global MOVE_DISTANCE_Y
        MOVE_DISTANCE_Y *= -1

    def bounce_x(self):
        global MOVE_DISTANCE_X
        MOVE_DISTANCE_X *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.02
        self.bounce_x()
