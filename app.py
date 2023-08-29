from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "home"

@app.route("/post")
def post():
    return "post page"