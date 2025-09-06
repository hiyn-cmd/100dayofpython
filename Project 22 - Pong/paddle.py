from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cordinates):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len= 1, stretch_wid=5)
        self.penup()
        self.speed("fastest")
        self.goto(cordinates)

    def up(self):
        prev_cord = self.ycor()
        self.sety(prev_cord + 20)

    def down(self):
        prev_cord = self.ycor()
        self.sety(prev_cord - 20)