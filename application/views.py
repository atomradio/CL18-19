#!/usr/bin/python3
from application import app


@app.route("/")
def index():
    return "Initial Page"
