from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="𝚃𝚒𝚖𝚎𝚛")
    REPS = 0
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        title_label.config(text="Break!", font=(FONT_NAME, 40, "bold"), fg=YELLOW, bg=GREEN)
        count_down(long_break)
    elif REPS % 2 == 0:
        title_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=GREEN)
        count_down(short_break)
    else:
        title_label.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=RED, bg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for i in range(work_sessions):
            marks += "☑"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

title_label = Label(text="𝚃𝚒𝚖𝚎𝚛", font=("Arial", 40, "bold"), fg=RED, bg=GREEN)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check = Label(font=("Arial", 24, "bold"), fg=RED, bg=GREEN)
check.grid(column=1, row=3)
window.mainloop()
