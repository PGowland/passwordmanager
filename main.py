from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_info():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "Email/Username": user,
        "Password": password
    }}

    if len(website) != 0 and len(user) != 0 and len(password) != 0:
        try:
            with open("password_storage.json", 'r') as pass_doc:
                data = json.load(pass_doc)
                data.update(new_data)
            with open("password_storage.json", 'w') as pass_doc:
                json.dump(data, pass_doc, indent=4)
        except FileNotFoundError:
            with open("password_storage.json", 'w') as pass_doc:
                json.dump(new_data, pass_doc, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="ERROR", message="One or more fields are empty")


def search_data():
    website = website_entry.get()
    with open("password_storage.json", 'r') as pass_doc:
        data = json.load(pass_doc)
        messagebox.showinfo(title=website,
                            message=f"Email/Username: {data[website]['Email/Username']}"
                                    f"\nPassword: {data[website]['Password']}"
                            )

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(80, 80, image=logo_pic)
canvas.grid(row=0, column=1)

website_text = Label(text="Website:")
website_text.grid(row=1, column=0)
user_text = Label(text="Email/Username:")
user_text.grid(row=2, column=0)
password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, columnspan=3, sticky="w")
website_entry.focus()
user_entry = Entry(width=47)
user_entry.grid(row=2, column=1, columnspan=2, sticky="w")
user_entry.insert(0, "yourusualemail@gmail.com")
password_entry = Entry(width=28)
password_entry.grid(row=3, column=1, sticky="w")
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=1, columnspan=2, sticky="e")
add_button = Button(text="Add", command=add_info, width=40)
add_button.grid(row=4, column=1)
search_button = Button(text="Search", command=search_data, width=10)
search_button.grid(row=1, column=1, columnspan=2, sticky="e")

window.mainloop()
