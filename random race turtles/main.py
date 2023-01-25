from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
x = -100
y = 0


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[y])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=x)
    all_turtles.append(new_turtle)
    x += 40
    y += 1

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner")

        rand_distance = randint(0, 10)
        turtle.fd(rand_distance)



screen.exitonclick()