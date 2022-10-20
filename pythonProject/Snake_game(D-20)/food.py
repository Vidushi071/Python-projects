import random
from turtle import Turtle


class Food(Turtle):
    # Turtle a superclass and food a subclass

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("red")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-370, 370)
        random_y = random.randint(-370, 370)
        self.goto(random_x, random_y)

