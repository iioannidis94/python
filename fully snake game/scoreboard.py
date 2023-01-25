from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.pu()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.current_score = 0
        self.score_update()

    def increase_score(self):
        self.current_score += 1
        self.score_update()
