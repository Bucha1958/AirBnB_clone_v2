#!/usr/bin/python3
"""
    Flask script
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    replace = text.replace("_", " ")
    return ("C {}".format(replace))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text='is cool'):
    replace = text.replace("_", " ")
    return ("Python {}".format(replace))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
