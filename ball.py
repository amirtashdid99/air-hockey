from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10
        self.move_speed = (0.1)

    def move(self):
        xball = self.xcor() + self.xmove
        yball = self.ycor() + self.ymove
        self.goto(xball, yball)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed*=0.9


    def reset(self):
        self.goto(0, 0)
        self.move_speed=0.1
        self.bounce_x()
