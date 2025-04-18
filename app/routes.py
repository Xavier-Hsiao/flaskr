from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm
from flask_login import current_user, login_user
import sqlalchemy as sa
from app.models import User

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
    # logined users should not get to login page
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()

    # GET request -> false
    # POST request -> true
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect("login")
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)