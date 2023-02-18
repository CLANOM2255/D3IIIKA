from flask import render_template
from . import app
from .forms import LoginForm, SignupForm

@app.route("/")
@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/login")
def login():
    form = LoginForm()
    if not form["nickname"] and not form["password"]:
        return "Саксесс"
    return render_template("login.html", form=form)

@app.route("/signup")
def signup():
    form = SignupForm()
    return render_template("signup.html", form=form)