from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


TMDB_API_KEY = "your-api-key"
TMDB_SEARCH_EP = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"<title: {self.title}>"

class RateMovieForm(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")



# db.create_all()
#
# new_movie = Movie(
#     title="Test",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()



@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    for movie in all_movies:
        movie.ranking = all_movies.index(movie) + 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    id = request.args.get('id')
    movie = Movie.query.get(id)
    form_rate_movie = RateMovieForm()
    if form_rate_movie.validate_on_submit():
        movie.rating = float(form_rate_movie.rating.data)
        movie.review = form_rate_movie.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form_rate_movie)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form_add_movie = AddMovieForm()
    if form_add_movie.validate_on_submit():
        movie_title = form_add_movie.title.data
        parameters = {
            "api_key":  TMDB_API_KEY,
            "query": movie_title
        }
        response = requests.get(url=TMDB_SEARCH_EP, params=parameters)
        data = response.json()
        movies = data['results']
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form_add_movie)

@app.route('/search')
def search():
    movie_id = request.args.get('id')
    parameters = {
        "api_key": TMDB_API_KEY,

    }
    response = requests.get(url="https://api.themoviedb.org/3/movie/"+movie_id, params=parameters)
    movie = response.json()
    new_movie = Movie(title=movie["title"],
                      year=movie['release_date'].split('-')[0],
                      description=movie['overview'],
                      img_url='https://image.tmdb.org/t/p/original/' + movie['poster_path'])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
