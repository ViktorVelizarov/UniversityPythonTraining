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
light = 0
humidity = 0
temperature = 0

minLight = 10000
minHumidity = 10000
minTemperature = 10000

maxLight = 0
maxHumidity = 0
maxTemperature = 0

avgLight = 0
avgHumidity = 0
avgTemperature = 0

totalLight = 0
totalHumidity = 0
totalTemperature = 0

measurementCount = 0

listOfMeasurments = []
listOfStats = [
    ("Min:", "", "", ""),
    ("Max:", "", "", ""),
    ("Avg:", "", "", "")
]


def findStats(currentLight, currentHumidity, currentTemp):
    global minLight, minHumidity, minTemperature
    global maxLight, maxHumidity, maxTemperature
    global avgLight, avgHumidity, avgTemperature
    global totalLight, totalHumidity, totalTemperature
    global measurementCount
    measurementCount = measurementCount + 1
    totalLight = totalLight + currentLight
    totalHumidity = totalHumidity + currentHumidity
    totalTemperature = currentTemp + totalTemperature

    avgLight = totalLight / measurementCount
    avgHumidity = totalHumidity / measurementCount
    avgTemperature = totalTemperature / measurementCount

    if (currentLight < minLight):
        minLight = currentLight
    if (currentHumidity < minHumidity):
        minHumidity = currentHumidity
    if (currentTemp < minTemperature):
        minTemperature = currentTemp

    if (currentLight > maxLight):
        maxLight = currentLight
    if (currentHumidity > maxHumidity):
        maxHumidity = currentHumidity
    if (currentTemp > maxTemperature):
        maxTemperature = currentTemp


def updateStats():
    global minLight, minHumidity, minTemperature
    global maxLight, maxHumidity, maxTemperature
    global avgLight, avgHumidity, avgTemperature
    avgLight = round(avgLight, 2)
    avgHumidity = round(avgHumidity, 2)
    avgTemperature = round(avgTemperature, 2)
    listOfStats[0] = ("Min:", minLight, minHumidity, minTemperature)
    listOfStats[1] = ("Max:", maxLight, maxHumidity, maxTemperature)
    listOfStats[2] = ("Avg:", avgLight, avgHumidity, avgTemperature)


def currentTime():
    rightNow = datetime.now()
    time = rightNow.strftime("%H:%M:%S")
    day = rightNow.strftime("%A")
    return time + "."


def LDRChanged(data):
    global light
    light = data[2]
    # print(data)


def Measure(data):
    global humidity, temperature
    # [report_type, error_value, pin, dht_type, humidity, temperature, timestamp]
    if (data[1] == 0):
        humidity = data[4]
        temperature = data[5]


app = Flask(__name__)


global board
board = CustomTelemetrix()
board.displayOn()
board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=Measure)
board.set_pin_mode_analog_input(
    LDRPIN, callback=LDRChanged, differential=10)
# Note: The differential defines the distance between the previous
#       and current light. If the difference is greater dan differential
#       then LDRChange() is called. This solution reduces noise.


@app.route('/')
def hello_world():
    global light, humidity, temperature
    global listOfMeasurments
    findStats(light, humidity, temperature)
    updateStats()
    listOfMeasurments.insert(
        0, (currentTime(), light, humidity, temperature))
    listOfMeasurments = listOfMeasurments[:10]
    return render_template('index.html', measurments=listOfMeasurments, stats=listOfStats)


app.run()
