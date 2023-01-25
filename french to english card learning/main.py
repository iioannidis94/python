from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pd.read_csv("data/words_to_learn.csv", encoding="utf-8")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv", encoding="utf-8")
    to_learn = original_data.to_dict(orient="records")
else:

    to_learn = data.to_dict(orient="records")


# ------------------------buttons functions-------------------


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=old_image)

    flip_timer = window.after(4000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=new_image)



# ----------------------------Make the GUI-------------------------------
# window GUI


window = Tk()
window.title("Flash Card Game")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, func=flip_card)

# Images
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
right_button = PhotoImage(file="images/right.png")
wrong_button = PhotoImage(file="images/wrong.png")


# images
new_image = PhotoImage(file="images/card_back.png")
old_image = PhotoImage(file="images/card_front.png")
# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=old_image)
# picture text
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
button_x = Button(image=wrong_button, highlightthickness=0, command=next_card)
button_x.grid(column=0, row=1)
button_v = Button(image=right_button, highlightthickness=0, command=is_known)
button_v.grid(column=1, row=1)

next_card()


window.mainloop()
