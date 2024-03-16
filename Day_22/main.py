from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard 
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game = True
while game:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
#detect colision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bouncey()

    if ball.xcor() > 380 or ball.xcor() < -380:
       ball.bouncex()

#detect colision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >330 or ball.distance(l_paddle) < 50 and ball.xcor() < 330: 
       ball.bouncex()

# detect if r paddle misses:
    if ball.xcor() > 380:
       scoreboard.l_point() 
       ball.reset_position()
       
# detect if r paddle misses:
    if ball.xcor() < -380:
       scoreboard.r_point() 
       ball.reset_position()

screen.exitonclick()