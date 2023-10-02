from flask import Flask
from flask import render_template
from datetime import datetime
import random


def currentTime():
    rightNow = datetime.now()
    time = rightNow.strftime("%I:%M%p")
    time = time.lstrip('0')
    time = time.lower()
    day = rightNow.strftime("%A")
    return "It is " + time + " on " + day + "."


def currentLight():
    return random.uniform(0, 1000)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', time=currentTime(),
                           light=currentLight())


app.run()
