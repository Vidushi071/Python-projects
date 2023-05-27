import json
import random
from tkinter import *
from tkinter import messagebox

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_num = random.randint(4, 7)
    num_num = random.randint(2, 4)
    sym_num = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(letter_num)]
    password_number = [random.choice(numbers) for _ in range(num_num)]
    password_symbols = [random.choice(symbols) for _ in range(sym_num)]

    password = password_number + password_symbols + password_letter

    random.shuffle(password)

    password_f = "" .join(password)

    password_input.insert(0, password_f)
    # used to copy it in the clipboard so can directly save it to the website where we want to write the new password
    pyperclip.copy(password_f)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_entry = website_input.get()
    email_entry = email_input.get()
    password_entry = password_input.get()
    new_data = {
        website_entry: {
            "email":email_entry,
            "password":password_entry,
        }
    }

    if len(website_entry) == 0 or len(password_entry) == 0 or len(email_entry) == 0:
        messagebox.showinfo(title="Oops", message="Kindly fill the details. You missed the one of the input boxes")

    else:
        is_ok = messagebox.askokcancel(title="confirmation box", message=f"Website: {website_entry}"
                                                                         f"\n Email:{email_entry}\n Password:{password_entry} \n Is it ok to save the data?")
        if is_ok:
            try:
                with open("data.json", "r") as data:
                    # Reading the old data
                    file_data = json.load(data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    # Saving the updating data
                    json.dump(new_data, data, indent=4)
            else:
                 # Updating the old data with the new data
                file_data.update(new_data)
                with open("data.json","w") as data:
                    # Saving the updating data
                    json.dump(file_data, data, indent=4)
            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- SEARCH DETAILS ------------------------------- #
def search():
    website_entry = website_input.get()
    try:
        with open("data.json", "r") as data:
            # Reading the old data
            file_data = json.load(data)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")

    else:
        if website_entry in file_data:
            email_data=file_data[website_entry]["email"]
            password_data = file_data[website_entry]["password"]
            messagebox.showinfo(title=f"{website_entry}",message=f"Email:{email_data}\n Password: {password_data}")
        else:
            messagebox.showinfo(title=f"{website_entry}", message="No details for this website found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1,  sticky="EW")
website_input.focus()

Email = Label(text="Email/Username:")
Email.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "vidushisharma071@gmail.com")

Password = Label(text="Password:")
Password.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

search_button =Button(text="Search",command=search)
search_button.grid(row=1,column=2,sticky="EW")

pass_button = Button(text="Generate Password", command=password_generator)
pass_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
window.mainloop()
