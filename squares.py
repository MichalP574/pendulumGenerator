from turtle import Turtle


class Squares(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_len=3, stretch_wid=2)
        self.penup()
        self.goto(position)
