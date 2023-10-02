from flask import Flask
from flask import render_template
from datetime import datetime
import random

listOfMeasurments = []


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
    global listOfMeasurments
    random_color = "#{:02x}{:02x}{:02x}".format(random.randint(
        0, 255), random.randint(0, 255), random.randint(0, 255))
    listOfMeasurments.insert(0, (currentTime(), currentLight(), random_color))
    listOfMeasurments = listOfMeasurments[:10]
    return render_template('index.html', measurments=listOfMeasurments)


app.run()
