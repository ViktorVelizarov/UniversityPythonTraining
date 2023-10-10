from fhict_cb_01.custom_telemetrix import CustomTelemetrix
from datetime import datetime
import time
import requests
light = 0
humidity = 0
temperature = 0
LDRPIN = 2  # analog pin A2
DHTPIN = 12  # digital pin


def currentTime():
    rightNow = datetime.now()
    time = rightNow.strftime("%H:%M:%S")
    day = rightNow.strftime("%A")
    return time + "."


def LDRChanged(data):
    global light
    light = data[2]


def Measure(data):
    global humidity, temperature
    if (data[1] == 0):
        humidity = data[4]
        temperature = data[5]


global board
board = CustomTelemetrix()
board.displayOn()
board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=Measure)
board.set_pin_mode_analog_input(
    LDRPIN, callback=LDRChanged, differential=10)


# Create an infinite loop
while True:
    print("\n\n*** Data sent succesfully ***\n")
    data = {'time': currentTime(), 'temperature': temperature,
            'light': light, "humidity": humidity}
    response = requests.post('http://localhost:5000/data', json=data)
    time.sleep(1)  # Wait for 1 second before repeating
