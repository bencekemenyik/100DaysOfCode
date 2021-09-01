from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# db.create_all()


@app.route('/')
def home():
    all_books = Books.query.all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:

        book = Books(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('home'))

@app.route('/edit', methods=['GET', 'POST'])
def edit():

    if request.method == "POST":
        id = request.form["id"]
        book = Books.query.get(id)
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    id = request.args.get('id')
    book = Books.query.get(id)
    return render_template('edit.html', book=book)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    book_to_delete = Books.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

