from flask import Flask
from flask import render_template
from datetime import datetime
import random
import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
LDRPIN = 2  # analog pin A2
DHTPIN = 12  # digital pin
# Initialized global variables

temperature = 0
listOfMeasurments = [{"10:20", "20C"},
                     {"10:21", "21C"},
                     {"10:22", "22C"},
                     {"10:23", "23C"}]


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', measurments=listOfMeasurments)


app.run()
