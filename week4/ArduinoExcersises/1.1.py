import time
from fhict_cb_01.custom_telemetrix import CustomTelemetrix
board = CustomTelemetrix()
PIN = 13

def setup():
    board.set_pin_mode_digital_output(PIN)

def loop():
    board.digital_write(PIN, 1)
    time.sleep(0.2)
    board.digital_write(PIN, 0)
    time.sleep(0.2)

setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:  # crtl+C
        print('shutdown')
        board.shutdown()
