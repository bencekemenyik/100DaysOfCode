from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------ NEW CARD GENERATOR ------------------------------ #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

words_to_learn = data.to_dict(orient="records")
card = {}

def flip_card():
    english_word = card["English"]
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")

def generate_new_card():
    global card, timer
    window.after_cancel(timer)
    card = random.choice(words_to_learn)  # this is a dict
    french_word = card["French"]
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    timer = window.after(3000, flip_card)

def generate_new_card_and_remove_known_card():
    words_to_learn.remove(card)
    file_data = pandas.DataFrame(words_to_learn)
    file_data.to_csv("data/words_to_learn.csv", index=False)
    generate_new_card()
# ------------------------------ UI SETUP ------------------------------ #

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=generate_new_card)
x_button.grid(column=0, row=1)


tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=generate_new_card_and_remove_known_card)
tick_button.grid(column=1, row=1)


generate_new_card()


























window.mainloop()