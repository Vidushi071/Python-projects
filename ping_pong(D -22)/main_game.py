from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.tracer(0)

line = Turtle()
line.color("white")
line.penup()
line.pensize(10)
line.goto(0, 300)
line.setheading(270)
while line.ycor() > -300:
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Scoreboard()


ping_ball = Ball()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ping_ball.ball_speed)
    ping_ball.move()

    if ping_ball.ycor() > 280 or ping_ball.ycor() < -280:
        ping_ball.bounce_y()


    if r_paddle.ycor() > 260 or r_paddle.ycor() < -260:
        r_paddle.boundary_r()

    if l_paddle.ycor() > 260 or l_paddle.ycor() < -260:
        l_paddle.boundary_l()


    if ping_ball.distance(r_paddle) < 50 and ping_ball.xcor() > 320 or ping_ball.distance(l_paddle) < 50 and ping_ball.xcor() < -320 :
        ping_ball.bounce_x()
        ping_ball.speed()

    #Detect if it misses the right paddle
    if ping_ball.xcor() > 380 :
        ping_ball.refresh()
        score.score_l()


    if ping_ball.xcor() <-380:
        ping_ball.refresh()
        score.score_r()

screen.exitonclick()
