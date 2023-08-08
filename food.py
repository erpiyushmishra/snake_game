from turtle import Turtle
from random import Random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random = Random()
        x_cor = random.randint(-280, 200)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)
