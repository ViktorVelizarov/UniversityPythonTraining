from flask import Flask
from flask import render_template
from datetime import datetime
import random
import time
import sys
import csv
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
LDRPIN = 2  # analog pin A2
DHTPIN = 12  # digital pin
# Initialized global variables

temperature = 0
listOfMeasurments = []


app = Flask(__name__)


def currentTime():
    rightNow = datetime.now()
    time = rightNow.strftime("%H:%M:%S")
    return time


def randomTemperature():
    temperature = round(random.uniform(5, 45), 2)
    return temperature


def addToFile():
    csv_filename = 'temperature_samples.csv'
    temp = randomTemperature()
    time = currentTime()
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(listOfMeasurments)


@app.route('/')
def hello_world():
    addToFile()
    global listOfMeasurments
    listOfMeasurments.insert(
        0, (currentTime(), randomTemperature()))
    listOfMeasurments = listOfMeasurments[:10]
    return render_template('index.html', measurments=listOfMeasurments)


app.run()
