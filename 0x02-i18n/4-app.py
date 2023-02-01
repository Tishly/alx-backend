#!/usr/bin/env python3
"""
    A Basic Babel app
"""
from flask import Flask, render_template, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config files for app variables
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'], locale=fr)
    def home() -> str:
    """Endpoint that routes user to the homepage"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """
        Determines the best match with supported languages
    """
    if g.get.lang_code not in app.config['LANGUAGES']:
        #g.lang_code = 'fr'
        #return g.lang_code
        return app.config['BABEL_DEFAULT_LOCALE']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
