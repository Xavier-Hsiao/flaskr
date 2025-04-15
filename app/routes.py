from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Xavier"} # fake user data
    posts = [
        {
            'author': {'username': 'Xavier'},
            'body': 'I love may cat so much!'
        },
        {
            'author': {'username': 'Cat'},
            'body': 'Just feed me and leave me alone!'
        }
    ] # fake posts data
    return render_template("index.html", title="Home", user=user, posts=posts)