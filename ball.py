from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len = 2, stretch_wid = 2)
        self.color('white')
        self.speed(1.5)
        self.refresh()
    
    # Resets the ball
    def refresh(self):
        self.goto(0, 0)

    # Setting the direction to a random angle
    def set_direction(self):
        self.setheading(randint(1, 360))
    
    # Moves the ball 15 steps 
    def move(self):
        self.forward(15)
