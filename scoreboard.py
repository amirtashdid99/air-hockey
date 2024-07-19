from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.hideturtle()
        self.rscore=0
        self.lscore=0
        self.update()

    def update(self):
        self.clear()
        self.goto (-100 , 200)
        self.write(self.lscore, align='center', font=('Arial', 80, 'normal'))
        self.goto(100 , 200)
        self.write(self.rscore, align='center', font=('Arial', 80, 'normal'))

    def lp(self):
        self.lscore += 1
        self.update()

    def rp(self):
        self.rscore += 1
        self.update()
