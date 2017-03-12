import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
BUTTON = 40
GREEN = 11
RED = 13
YELLOW = 15

gpio.setup(GREEN, gpio.OUT)
gpio.setup(RED, gpio.OUT)
gpio.setup(YELLOW, gpio.OUT)

gpio.setup(BUTTON, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.add_event_detect(BUTTON, gpio.RISING)
def leds(status):
    gpio.output(YELLOW, status)
    gpio.output(GREEN, status)
    gpio.output(RED, status)

def buttonCallback(pin):
    if gpio.input(pin) == 1:
        print "STOP"
        leds(True)
        time.sleep(0.2)
        leds(False)
        time.sleep(0.2)
        leds(True)
        time.sleep(0.2)
        leds(False)

gpio.add_event_callback(BUTTON, buttonCallback)
while 1:
    pass
