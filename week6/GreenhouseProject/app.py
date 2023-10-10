from flask import Flask
from flask import render_template

import random
import time
import sys
from flask import request, redirect
app = Flask(__name__)

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


@app.route('/data', methods=['POST'])
def receiveData():
    global listOfMeasurments
    data = request.get_json()
    sentTime = data['time']
    sentTemp = data['temperature']
    sentLight = data['light']
    sentHumid = data['humidity']
    listOfMeasurments.insert(
        0, (sentTime, sentLight, sentHumid, sentTemp, 5055121))
    listOfMeasurments = listOfMeasurments[:10]
    findStats(sentLight, sentHumid, sentTemp)
    updateStats()


@app.route('/sensorChoice', methods=['POST'])
def receiveChoice():
    sensor = request.form['sensor']
    if sensor == 'light':
        return redirect('/lightSensor')
    if sensor == 'temp':
        return redirect('/temperatureSensor')
    if sensor == 'humidity':
        return redirect('/humiditySensor')
    if sensor == 'all':
        return redirect('/allSensors')


@app.route('/allSensors')
def allSensors():
    return render_template('allSensors.html', measurments=listOfMeasurments, stats=listOfStats)


@app.route('/temperatureSensor')
def temperatureSensor():
    return render_template('oneSensor.html', selectedSensor="temperature", measurments=listOfMeasurments, stats=listOfStats)


@app.route('/lightSensor')
def lightSensor():
    return render_template('oneSensor.html', selectedSensor="light", measurments=listOfMeasurments, stats=listOfStats)


@app.route('/humiditySensor')
def humiditySensor():
    return render_template('oneSensor.html', selectedSensor="humidity", measurments=listOfMeasurments, stats=listOfStats)


@app.route('/')
def appStart():
    return render_template('form.html')


app.run()
