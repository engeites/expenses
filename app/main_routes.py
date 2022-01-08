from time import time

from flask import render_template, jsonify

from app import app


@app.route("/")
def index():
    """
    Index page just for fun
    :return:
    """
    return render_template('index.html')


@app.route("/time")
def return_time():
    """
    This endpoint returns server's current time in milliseconds
    :return:
    """
    return jsonify({'current time': time()})
