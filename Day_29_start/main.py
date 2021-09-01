from tkinter import *
from tkinter import messagebox
import random
import json

FG_COLOR = "#D4483B"
BG_COLOR = "#161616"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)
# ---------------------------- PASSWORD FINDER ------------------------------- #

def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    website = website_entry.get().strip().title()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Some fields were left empty. Fix it please.")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)


# Labels
website_label = Label(text="Website:", fg=FG_COLOR, bg=BG_COLOR)
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", fg=FG_COLOR, bg=BG_COLOR)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", fg=FG_COLOR, bg=BG_COLOR)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=30, bg=BG_COLOR, fg=FG_COLOR)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=30, bg=BG_COLOR, fg=FG_COLOR)
email_entry.grid(column=1, row=2)


password_entry = Entry(width=30, bg=BG_COLOR, fg=FG_COLOR)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator, width=15, bg=BG_COLOR, fg=FG_COLOR)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_to_file, bg=BG_COLOR, fg=FG_COLOR)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, width=15, bg=BG_COLOR, fg=FG_COLOR)
search_button.grid(column=2, row=1)

# Canvas
logo_png = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

window.mainloop()
