from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

winner = ''
player_1 = input('Player 1: ')
player_2 = input('Player 2: ')

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

ball = Ball()
paddle_2 = Paddle(320, 0)
paddle_1 = Paddle(-320, 0)
scoreboard = Scoreboard(player_1, player_2)

screen.listen()
screen.onkey(paddle_2.move_up, 'Up')
screen.onkey(paddle_2.move_down, 'Down')
screen.onkey(paddle_1.move_up, 'w')
screen.onkey(paddle_1.move_down, 's')

ball.set_direction()

def main():

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.05)
        ball.move()

        # Check for collisions
        if ball.ycor() >= 270 or ball.ycor() <= -270:
            current_angle = ball.heading()
            if 0 < current_angle < 180:
                ball.setheading(0 - current_angle)
            else:
                ball.setheading(360 - current_angle)

        if (ball.xcor() <= paddle_1.xcor() + 30 
            and paddle_1.ycor() - 80 <= ball.ycor() <= paddle_1.ycor() + 80) \
            or (paddle_2.xcor() - 30 <= ball.xcor() \
            and paddle_2.ycor() - 80 <= ball.ycor() <= paddle_2.ycor() + 80):

            if ball.xcor() < paddle_1.xcor() + 30 and ball.heading() > 0:
                ball.setx(paddle_1.xcor() + 30)
            elif ball.xcor() > paddle_2.xcor() - 30 and ball.heading() < 180:
                ball.setx(paddle_2.xcor() - 30)

            if 0 < ball.heading() < 180:
                ball.setheading(180 - ball.heading())
            else:
                ball.setheading(540 - ball.heading())

        # Check for scores
        if ball.xcor() >= 350 or ball.xcor() <= -350:    
            if ball.xcor() >= 350:
                scoreboard.increase_score_1()
            elif ball.xcor() <= -350:
                scoreboard.increase_score_2()
            ball.refresh()
            ball.set_direction()
            paddle_1.refresh(-320, 0)
            paddle_2.refresh(320, 0)

            if scoreboard.score_1 == 7:
                winner = scoreboard.player_1
                game_is_on = False
            elif scoreboard.score_2 == 7:
                winner = scoreboard.player_2
                game_is_on = False

    scoreboard.game_over(winner)
    screen.exitonclick()

if __name__ == "__main__":
    main()