#!/usr/bin/env python3
from flask import Flask, render_template
"""A Basic Flask Application with one endpoint"""

app = Flask(__name__)

app.route("/")
def home():
    """Endpoint that routes user to the homepage"""
   return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
