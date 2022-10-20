from turtle import  Turtle

MOVE_DISTANCE = 10

class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinate)
        self.go_up()
        self.go_down()

    def boundary_r(self):
        self.goto(350, 0)

    def boundary_l(self):
        self.goto(-350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
