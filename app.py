import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from config import Config
from database import db
from auth import login_required

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if (
            username == app.config["ADMIN_USERNAME"]
            and
            password == app.config["ADMIN_PASSWORD"]
        ):
            session["logged_in"] = True
            return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=False
    )
