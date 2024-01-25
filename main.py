from random import randint
from flask import Flask, render_template
from datetime import datetime
from datetime import date
app = Flask(__name__)

@app.route('/')
def index() -> str:

    return render_template("index.html", name="Nikita",)

@app.route('/user/<username>/<age>')
def user_info(username: str, age: str) -> str:
    info = (f'<h1>Hi {username}</h1><br>'
            f'<p>You are {age} years old<p>')
    return info
@app.route('/time/')
def time() -> str:
    now = datetime.now()
    current_date = str(date.today())[6:7]
    current_date = int(current_date)
    if current_date <= 6:
        mouths_to_summer = 6 - current_date
    elif current_date > 6 and current_date < 9:
        mouths_to_summer = 0
    else:
        mouths_to_summer = current_date - 6
    print(mouths_to_summer)
    return render_template("time.html", now=now.strftime("%H:%M:%S"), mouths=mouths_to_summer)
    
@app.route('/random/')
def random() -> str:
    return render_template("random.html", num=randint(0, 99))

app.run(debug=True)
