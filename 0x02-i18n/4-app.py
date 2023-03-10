#!/usr/bin/env python3
"""
    A Basic Babel app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """
    Config files for app variables
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'], strict_slashes=False)
def home() -> str:
    """Endpoint that routes user to the homepage"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """
        Ensures URL contains matching translation
    else:
        Determines the best match within supported languages
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
