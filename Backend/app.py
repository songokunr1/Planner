from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)
app.secret_key = 'it is hard to hack!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("base.html")


@app.route("/message", methods=['GET', 'POST'])
def message():
    req = request.json
    print(req)
    return render_template("base.html")


if __name__ == '__main__':
    app.run(port=8030, debug=True)