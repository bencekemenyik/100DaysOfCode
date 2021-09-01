from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f"<b> {function()} </b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em> {function()} </em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u> {function()} </u>"
    return wrapper_function



@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width="200">'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route("/username/<name>")
def greet(name):
    return f"Hello there {name}"


def print_kenyer():
    return "kenyer"

if __name__ == "__main__":
    app.run(debug=True)

