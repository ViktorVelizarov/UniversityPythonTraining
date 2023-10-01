import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

buttonPin1 = 8
buttonPin2 = 9
redPin = 4
bluePin = 6

buttonStateOne = 0
buttonStateTwo = 0


def setup():
    global board
    board = CustomTelemetrix()
    board.set_pin_mode_digital_output(redPin)
    board.set_pin_mode_digital_output(bluePin)
    board.set_pin_mode_digital_input_pullup(buttonPin1)
    board.set_pin_mode_digital_input_pullup(buttonPin2)
    time.sleep(0.1)


def loop():
    level1, time_stamp1 = board.digital_read(buttonPin1)
    level2, time_stamp2 = board.digital_read(buttonPin2)
    print(level1, level2)
    time.sleep(0.01)  # Give Firmata some time to handle protocol.
    if level1 == 0:
        board.digital_write(redPin, 1)
    else:
        board.digital_write(redPin, 0)

    if level2 == 0:
        board.digital_write(bluePin, 1)
    else:
        board.digital_write(bluePin, 0)


setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:  # ctrl+C
        print('shutdown')
        board.shutdown()
        sys.exit(0)
