import json
import tkinter as tk
from random import choice, randint, shuffle
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    application = application_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = (f"{application}, {user}, {password}")

    if len(application) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        file_location = "data.txt"
        with open(file_location, "a") as data_file:
            data_file.write(new_data + "\n")
            application_entry.delete(0, tk.END)
            user_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        messagebox.showinfo(title="Success!", message=(
            f"Data has been saved for {user}"))


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

title = tk.Label(text="Password Manager")
title.grid(column=1, row=1)
application = tk.Label(text="Application Name")
application.grid(column=0, row=2)
application_entry = tk.Entry(width=35)
application_entry.grid(column=1, row=2, columnspan=2)
user = tk.Label(text="User Name / Email")
user.grid(column=0, row=3)
user_entry = tk.Entry(width=35)
user_entry.grid(column=1, row=3, columnspan=2)
password = tk.Label(text="Password")
password.grid(column=0, row=4)
password_entry = tk.Entry(width=35)
password_entry.grid(column=1, row=4, columnspan=2)

generate_password = tk.Button(
    text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=4)

add = tk.Button(text="Add", command=save)
add.grid(column=1, row=5)


window.mainloop()
