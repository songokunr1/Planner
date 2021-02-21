from flask import Flask, render_template, url_for, request
import requests
from . import app
import json
import redis
from rq import Queue
import time

r = redis.Redis(host='rq-server', port=6379, decode_responses=True)
q = Queue(connection=r)

def background_task(n):

    """ Function that returns len(n) and simulates a delay """

    delay = 2

    print("Task running")
    print(f"Simulating a {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)


@app.route("/task")
def task():

    if request.args.get("n"):
        print("hejo")
        job = q.enqueue(background_task, request.args.get("n"))

        return f"Task ({job.id}) added to queue at {job.enqueued_at}"

    return "No value for count provided"


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("base.html")


@app.route("/message", methods=['GET', 'POST'])
def message():
    req = request.json
    print(req)
    return render_template("base.html")

@app.route("/ba", methods=['GET'])
def show_data():
    json_data = {
        "name": "ivanleoncz",
        "role": "Software Developer"
    }
    return json.dumps(json_data)


@app.route("/ba2", methods=['GET'])
def get_data():
    r = app.test_client().get("/ba")
    print(json.loads(r.data))
    return render_template("base.html")

