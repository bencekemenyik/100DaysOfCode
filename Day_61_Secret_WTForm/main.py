from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

app.secret_key = "your-secret-key"

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="Don't leave email field empty"), Email(message="Please enter a valid email.")])
    password = PasswordField(label='Password', validators=[DataRequired(message="Don't leave password field empty"), Length(min=8, message="Please type in a password that is at least 8 characters long")])
    submit = SubmitField(label='Log in')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)