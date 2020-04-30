from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask Versioning"

@app.route("/version")
def version():
    return "Version 1.1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)