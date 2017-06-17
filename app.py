from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/core")
def hiyumi():
    return "What's up Yumi!"