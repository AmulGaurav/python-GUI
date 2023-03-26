from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if (ball.distance(l_paddle) < 50 and ball.xcor() <= -360) or (ball.distance(r_paddle) < 50 and ball.xcor() >= 360):
        ball.bounce_x()

    # Detect when R paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect when L paddle misses.
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
