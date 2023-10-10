from flask import Flask
from flask import render_template
from datetime import datetime
from flask import request, redirect
import random
import time
import sys
import csv
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
LDRPIN = 2  # analog pin A2
DHTPIN = 12  # digital pin
# Initialized global variables

temperature = 0
totalTemperature = 0
count = 0
avgTemperature = 0
listOfMeasurments = []


app = Flask(__name__)


def currentTime():
    rightNow = datetime.now()
    time = rightNow.strftime("%H:%M:%S")
    return time


def randomTemperature():
    temperature = round(random.uniform(5, 45), 2)
    return temperature


@app.route('/addMeasurment', methods=['POST'])
def addMeasurment():
    global listOfMeasurments
    global count
    global avgTemperature
    global totalTemperature
    count = count + 1
    
    data = request.get_json()
    sentTime = data['time']
    sentTemp = data['temp']
    totalTemperature = totalTemperature + sentTemp
    
    listOfMeasurments.insert(
        0, (sentTime, sentTemp))

    listOfMeasurments = listOfMeasurments[:10]
    avgTemperature = totalTemperature / count


@app.route('/')
def hello_world():
    global listOfMeasurments
    return render_template('index.html', measurments=listOfMeasurments, average = avgTemperature)


app.run()
