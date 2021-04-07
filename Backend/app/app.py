from flask import Flask, render_template, url_for, request, jsonify
import requests
# from . import create_test_app
import json
import redis
from rq import Queue
import time
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
r = redis.Redis(host='rq-server', port=6379, decode_responses=True)
q = Queue(connection=r)

def example(seconds):
    print('Starting task')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Task completed')




def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push() # this does the binding
    return app

app = create_test_app()




def background_task(n):

    """ Function that returns len(n) and simulates a delay """

    delay = 1

    print("Task running")
    print(f"Simulating a {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)


@app.route("/task")
def task():
    task = request.args.get("n")
    print(task)
    if task:
        print("hejo")
        job = q.enqueue('app.tasks.background_task', request.args.get("n"))
        print(job.get_id())
        return f"Task ({job.id}) added to queue at {job.enqueued_at}"

    return "No value for count provided"

@app.route('/status/<job_id>')
def job_status(job_id):
    print(job_id)
    job = q.fetch_job(r"f66b4ef3-446c-47a8-9156-ee82d6ff5442")
    if job is None:
        response = {'status': 'unknown'}
    else:
        response = {
            'status': job.get_status(),
            'result': job.result,
        }
        if job.is_failed:
            response['message'] = job.exc_info.strip().split('\n')[-1]
    return jsonify(response)


@app.route("/create_task", methods=['GET', 'POST'])
def create_task():
    # task = request.form.get('task')
    job = q.enqueue('app.tasks.background_task', 5)
    print(job.get_id())
    return jsonify({}), 202, {'Location': url_for('job_status', job_id=job.get_id())}



@app.route("/", methods=['GET', 'POST'])
def index():
    job = q.enqueue('app.tasks.example', 23)
    print(job.get_id())
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
        "role": "Software Developer",
        "wa": "ha",
        "ba": "udalo sie"
    }
    return json.dumps(json_data)


@app.route("/ba2", methods=['GET'])
def get_data():
    r = app.test_client().get("/ba")
    print(json.loads(r.data))
    print('hejo')
    return render_template("base.html")

@app.route("/ba3", methods=['GET'])
def get_data2():
    r = app.test_client().get("/ba")
    print(json.loads(r.data))
    print('hejo')
    print("hejoa")
    return render_template("base.html")

if __name__ == '__main__':
    app.run(debug=True, port=8030)