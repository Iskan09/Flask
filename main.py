from random import randint
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index() -> str:
    return render_template("index.html", name="Nikita")

@app.route('/user/<username>/<age>')
def user_info(username, age):
    info = (f'<h1>Hi {username}</h1><br>'
            f'<p>You are {age} years old<p>')
    return info
@app.route('/time/')
def time() -> str:
    return render_template("time.html", now=datetime.now().time())
    
@app.route('/random/')
def random() -> str:
    return render_template("random.html", num=randint(0, 5))

app.run(debug=True)
