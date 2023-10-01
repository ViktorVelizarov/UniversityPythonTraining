from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time

POTPIN = 0  # Analog pin A0
ledpin = 6  # Digital pin 6


potValue = 0
mappedValue = 0
board = None


def setup():
    global board
    board = CustomTelemetrix()
    board.set_pin_mode_analog_input(POTPIN)
    board.set_pin_mode_analog_output(ledpin)
    time.sleep(0.3)


def loop():
    global potValue, mappedValue
    potValue, timestamp = board.analog_read(POTPIN)
    mappedValue = int(potValue * 255 / 1023)
    print(mappedValue)
    print(potValue)  # Extract the first value from the list
    board.analog_write(ledpin, mappedValue)
    time.sleep(0.1)


setup()
try:
    while True:
        loop()
except KeyboardInterrupt:
    print("Shutdown")
    board.shutdown()
