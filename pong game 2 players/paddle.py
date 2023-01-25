from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_x):
        super().__init__()
        self.new_y = None
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_x, y=0)

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)

