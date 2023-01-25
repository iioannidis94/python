from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '.', '{', '}', '[', ']', '|']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 5))]
    password_list += [choice(numbers) for _ in range(randint(2, 5))]

    shuffle(password_list)

    password_rand = "".join(password_list)

    pass_entry.insert(0, password_rand)
    pyperclip.copy(password_rand)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_file():

    web = web_entry.get().title()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": password,
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please fill all the fields to proceed")

    else:
        is_ok = messagebox.askokcancel(title=web, message=f"there are the details you entered: \n Email: {email}\n "
                                                  f"Password: {password}\n Is is ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # reading old data_file
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating old data_file with new data_file
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # saving updated data_file
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# -------------------------------------SEARCH-------------------------------------#


def find_password():
    web = web_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website You are looking for.")


# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)


label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Entries
web_entry = Entry(width=32)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "r4z0r3583@gmail.com")

pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)

# Buttons
generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2)

add = Button(text="Add", width=44, command=save_file)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=15, command=find_password)
search.grid(row=1, column=2)

window.mainloop()
