from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<html>Hello World! KKKK</html>"


@app.route("/admin")
def hello_world():
    return "<html>Hello Admin! KKKK</html>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
