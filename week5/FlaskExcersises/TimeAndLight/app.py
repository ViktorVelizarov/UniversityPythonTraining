from flask import Flask
from flask import render_template
from datetime import datetime


def currentTime():
    rightNow = datetime.now()
    time = rightNow.strftime("%I:%M%p")
    time = time.lstrip('0')
    time = time.lower()
    day = rightNow.strftime("%A")

    return "It is " + time + " on " + day + "."


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', time=currentTime())


app.run()
