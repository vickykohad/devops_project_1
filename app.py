from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
        return " i am workin in HPe from US "

@app.route("/phone")
def lwphone():
        return "9999900000"

app.run(host="0.0.0.0")
