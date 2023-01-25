from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

is_equal = Label(text="is equal to", font=("Arial", 24))
is_equal.grid(column=0, row=1)
is_equal.config(padx=10, pady=10)

miles = Label(text="Miles", font=("Arial", 24))
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)

km = Label(text="Km", font=("Arial", 24))
km.grid(column=2, row=1)
km.config(padx=10, pady=10)


km_result = Label(text="0", font=("Arial", 24))
km_result.config(padx=10, pady=10)
km_result.grid(column=1, row=1)


def button_clicked():
    a = float(input.get())
    res = a * 1.609
    km_result["text"] = res


input = Entry(width=10)
input.grid(column=1, row=0)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

window.mainloop()
