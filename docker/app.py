import redis
import sys

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route("/")
def root():
    data = {}

    for key in cache.keys():
        key = key.decode("utf-8")
        value = cache.get(key).decode("utf-8")

        data[key] = value

    return render_template("home.html", keys=data)


@app.route("/add", methods=["post"])
def add():
    key = request.form.get('key', None)
    value = request.form.get('value', None)

    if key is not None and value is not None:
        cache.set(key, value)

    return redirect("/", code=302)
