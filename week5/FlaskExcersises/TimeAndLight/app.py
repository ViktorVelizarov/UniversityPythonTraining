from flask import Flask
from flask import render_template
from datetime import datetime
import random


def currentTime():
    rightNow = datetime.now()
    time = rightNow.strftime("%H:%M:%S")
    day = rightNow.strftime("%A")
    return time + "."


def currentLight():
    return random.uniform(0, 1000)


app = Flask(__name__)


@app.route('/')
def hello_world():
    random_color = "#{:02x}{:02x}{:02x}".format(random.randint(
        0, 255), random.randint(0, 255), random.randint(0, 255))

    return render_template('index.html', time=currentTime(),
                           light=currentLight(),  random_color=random_color)


app.run()
