#!/usr/bin/env python3
"""
    A Basic Babel app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods = [GET])
def home() -> str:
    """Endpoint that routes user to the homepage"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
