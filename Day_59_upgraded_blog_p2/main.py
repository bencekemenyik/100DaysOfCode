from flask import Flask, render_template, request
import requests
from smtplib import SMTP


app = Flask(__name__)

all_blog_posts = requests.get(url="https://api.npoint.io/88c2c1f644ef334058be").json()




@app.route('/')
def home():
    return render_template('index.html', blog_posts=all_blog_posts)

@app.route('/index')
def also_home():
    return home()

@app.route('/post/<int:blog_id>')
def post(blog_id):
    index = blog_id - 1
    return render_template("post.html", blog_post=all_blog_posts[index])

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "GET":
        return render_template("contact.html", req_method=request.method)
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    with SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user="your-email", password="your-password")
        connection.sendmail(from_addr="your-email", to_addrs="your-email",
                            msg=f"Subject:Message from blog website\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
    return render_template("contact.html", req_method=request.method)



if __name__ == "__main__":
    app.run(debug=True)