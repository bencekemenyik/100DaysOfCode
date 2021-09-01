from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/bca7caa80bae33aded94")
    all_blog = response.json()
    return render_template("index.html", blog_posts=all_blog)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    response = requests.get(url="https://api.npoint.io/bca7caa80bae33aded94")
    all_blog = response.json()
    return render_template("post.html", blog_post=all_blog[blog_id-1])

if __name__ == "__main__":
    app.run(debug=True)
