from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

   def __init__(self):
       self.segments = []
       self.create_snake()
       self.head = self.segments[0]



   def create_snake(self):
        for position in STARTING_POSITION:
            self.add_box(position)

   def add_box(self, position):
       new_box = Turtle(shape="square")
       new_box.penup()
       new_box.color("white")
       new_box.goto(position)
       self.segments.append(new_box)

   def extend(self):
       self.add_box(self.segments[-1].position())

   def reset(self):
       for seg in self.segments:
           seg.goto(1500, 1500)

       self.segments.clear()
       self.create_snake()
       self.head = self.segments[0]

   def move(self):
       for box_num in range(len(self.segments) - 1, 0, -1):
           new_x = self.segments[box_num - 1].xcor()
           new_y = self.segments[box_num - 1].ycor()
           self.segments[box_num].goto(new_x, new_y)
       self.head.forward(MOVE_DISTANCE)


   def up(self):
       if self.head.heading() != DOWN:
        self.head.setheading(UP)


   def down(self):
       if self.head.heading() != UP:
        self.head.setheading(DOWN)

   def left(self):

       if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)

   def right(self):

       if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)
