from turtle import Turtle

class Paddle(Turtle):
    paddles=[]
    def __init__(self):
        super().__init__()

        self.shape('square')
        self.color('white')
        self.penup()

        self.speed(0)
        self.turtlesize(5,1)
        self.paddles.append(self)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
