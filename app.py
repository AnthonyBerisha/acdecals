from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/post")
def post():
    return render_template("post.html")