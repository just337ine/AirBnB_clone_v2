#!/usr/bin/python3
"""A script that starts a Flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_hbnb(text):
    text_result = text.replace('_', ' ')
    return f'C {text_result}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)