#!/usr/bin/env python3
"""A Basic Flask Application with one endpoint"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def home():
    """Endpoint that routes user to the homepage"""
    return render_template("0-index.html")


class Config(object):
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


@babel.localselector
def get_locale():
    return request.accept_languages.best_match(Config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
