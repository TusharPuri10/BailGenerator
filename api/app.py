from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods=['GET'])
def index():
    return "<p>Hello sir</p>"