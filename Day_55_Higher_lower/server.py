from flask import Flask
import random

app = Flask(__name__)

rnd_number = random.randint(0, 9)


@app.route('/')
def higher_lower_text():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:guessed_number>')
def display_text_based_on_guess(guessed_number):
    if guessed_number == rnd_number:
        return "<h1 style='color: green'>You found me</h1>" \
           "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif guessed_number < rnd_number:
        return "<h1 style='color: red'>Too low, try again</h1>" \
           "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color: purple'>Too high, try again</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"



if __name__ == "__main__":
    app.run(debug=True)