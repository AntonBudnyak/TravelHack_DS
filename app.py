from flask import Flask


app = Flask(__name__)
app.debug = True


a = {"items": [1, 2, 3]}


@app.route('/')
def hello_world():
    return say_hello()


def say_hello():
    return a

