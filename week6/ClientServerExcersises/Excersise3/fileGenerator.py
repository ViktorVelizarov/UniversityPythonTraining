
from datetime import datetime
import random
import csv
import requests
import time


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
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([currentTime(), randomTemperature()])


# Create an infinite loop
while True:
    print("\n\n*** fileGenerator ***\n")
    data = {'time': currentTime(), 'temp': randomTemperature()}
    response = requests.post('http://localhost:5000/addMeasurment', json=data)
    addToFile()
    time.sleep(1)  # Wait for 1 second before repeating
