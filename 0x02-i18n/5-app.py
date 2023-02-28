#!/usr/bin/env python3
"""
    A Basic Babel app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


users = {1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
         2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
         3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
         4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


class Config(object):
    """
    Config files for app variables
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.before_request
def before_request() -> None:
    """
        Mock test that checks if user is authorized before requesting data
    """
    user = get_user()
    g.user = user


def get_user() -> Union[Dict, None]:
    """
        Retrieves a user data based on id passed to URL
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id), None)
    return None

    return users.id


@app.route("/", methods=['GET'], strict_slashes=False)
def home() -> str:
    """Endpoint that routes user to the homepage"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
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
    app.run(host='0.0.0.0', port=5000)
