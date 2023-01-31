#!/usr/bin/env python3
"""A Basic Flask Application with one endpoint"""
from flask import Flask, render_template


app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def home():
    """Endpoint that routes user to the homepage"""
    return render_templatei("0-index.html")


class Config():
    LANGUAGES =["en", "fr"]


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
