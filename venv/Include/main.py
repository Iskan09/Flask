from flask import Flask

app = Flask(__name__)

@app.route("/")
def index() -> str:
    return '<h1>Hello World</h1>'

@app.route("/user/<username>/<age>")
def userinfo(username, age):
    info = (f"<h1>Hi, {username}</h1><br>"
            f"<h1>Y are {age} years old<h1/>")
    return info

app.run(debug=True)