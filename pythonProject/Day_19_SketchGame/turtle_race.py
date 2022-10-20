import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter the color")

color = ["red", "orange", "blue", "purple", "green", "yellow"]
y_pos = -120
all_turtles = []
race_is_on=True

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    y_pos = y_pos + 30
    new_turtle.goto(x=-230, y=y_pos)
    all_turtles.append(new_turtle)


while race_is_on:

    for turtle in all_turtles:

        if turtle.xcor() > 220:
            winning_color= turtle.pencolor()
            race_is_on = False
            if winning_color == user_bet:
                print(f"You Won! The {winning_color} turtle won the race .")
            else:
                print(f"You Lost! The {winning_color} turtle won the race .")
        turtle.forward(random.randint(0, 10))
print(user_bet)

screen.exitonclick()























