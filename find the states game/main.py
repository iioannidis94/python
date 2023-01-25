import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

data_us = pandas.read_csv("50_states.csv")
data_list = data_us["state"].to_list()
guessed_states = []
turtle.shape(image)

# count the correct answers
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = [state for state in data_list if state not in guessed_states]
        missing = pandas.DataFrame(missing_states)
        missing.to_csv("states_to_learn.csv")
        break

    if answer_state in data_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data_us[data_us.state == answer_state]
        # need int x, y
        t.goto(int(state_data.x), int(state_data.y))
        # get the state data alone with .item()
        t.write(state_data.state.item())


screen.exitonclick()
