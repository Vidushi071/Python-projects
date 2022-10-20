import time
from turtle import Screen

from food import Food
from score import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
player_name = screen.textinput(title="Player", prompt="Enter player's name :")
with open("name.txt", mode='w') as player:
    player.write(player_name)

score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# player_name = Turtle()
# p_name =Turtle()
# player_name.color("white")
# p_name =  screen.textinput(title="Player", prompt="Enter player name :")
# player_name.write(f"Player{p_name}", align="center", font=("Arial", 22, "normal"))
#
# player_name.hideturtle()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    #  Detect collision with wall

    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:

        score.reset()
        snake.reset()

    # Detect collision with snake tail

    for segment in snake.segments[1:]:  # python slicing
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()