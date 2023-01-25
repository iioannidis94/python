from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=900, height=700)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle(400)
r_paddle = Paddle(-400)
ball = Ball()
score = Score()


screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() > 370 or ball.distance(r_paddle) < 50 and ball.xcor() < -370:
        ball.bounce_x()
    # right miss

    if ball.xcor() > 430:
        ball.refresh()
        score.l_point()

    if ball.xcor() < -430:
        ball.refresh()
        score.r_point()


screen.exitonclick()
