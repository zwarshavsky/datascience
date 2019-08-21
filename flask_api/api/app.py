from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Welcome to the data science api for Music-Meteorology.com"


if __name__ == '__main__':
    app.run(debug=True)
