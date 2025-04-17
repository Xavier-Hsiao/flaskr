from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # GET request -> false
    # POST request -> true
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)