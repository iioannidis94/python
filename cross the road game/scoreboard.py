from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.pu()
        self.color("black")
        self.hideturtle()
        self.goto(-280, 250)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER. ", align="center", font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.update_scoreboard()