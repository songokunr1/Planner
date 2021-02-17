from flask import Flask, render_template, url_for, request
import requests
from Backend import app


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("base.html")


@app.route("/message", methods=['GET', 'POST'])
def message():
    req = request.json
    print(req)
    return render_template("base.html")

