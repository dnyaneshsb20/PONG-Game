from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

def play_game():
    ball.reset_position()
    scoreboard.reset_game()
    global is_game_on
    is_game_on = True

    while is_game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Paddle collision
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
           (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Right miss
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Left miss
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        # Win condition
        if scoreboard.l_score >= 5:
            scoreboard.game_over("Left Player")
            is_game_on = False
        elif scoreboard.r_score >= 5:
            scoreboard.game_over("Right Player")
            is_game_on = False

def restart_game():
    play_game()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkey(restart_game, "r")

play_game()
screen.mainloop()
