import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
board = CustomTelemetrix()
PIN1 = 4
PIN2 = 5
PIN3 = 6
PIN4 = 7


def setup():
    board.set_pin_mode_digital_output(PIN1)
    board.set_pin_mode_digital_output(PIN2)
    board.set_pin_mode_digital_output(PIN3)
    board.set_pin_mode_digital_output(PIN4)


def loop():
    board.digital_write(PIN1, 1)
    time.sleep(0.1)
    board.digital_write(PIN1, 0)

    board.digital_write(PIN2, 1)
    time.sleep(0.1)
    board.digital_write(PIN2, 0)

    board.digital_write(PIN3, 1)
    time.sleep(0.1)
    board.digital_write(PIN3, 0)

    board.digital_write(PIN4, 1)
    time.sleep(0.1)
    board.digital_write(PIN4, 0)


setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:  # crtl+C
        print('shutdown')
        board.shutdown()
        sys.exit(0)
