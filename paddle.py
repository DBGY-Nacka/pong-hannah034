from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position_x, position_y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len = 1, stretch_wid = 7)
        self.color('white')
        self.speed(1)
        self.refresh(position_x, position_y)

    # Resets the paddles at their starting position
    def refresh(self, position_x, position_y):
        self.goto(position_x, position_y)

    # Moves up in y-axis
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    # Moves down in y-axis
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 30)
