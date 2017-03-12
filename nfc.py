import RPi.GPIO as gpio
import MFRC522
import sys
import time

MIFAREReader = MFRC522.MFRC522()
GREEN = 11
RED = 13
YELLOW = 15
SERVO = 12

gpio.setup(GREEN, gpio.OUT, initial=gpio.LOW)
gpio.setup(RED, gpio.OUT, initial=gpio.LOW)
gpio.setup(YELLOW, gpio.OUT, initial=gpio.LOW)
gpio.setup(SERVO, gpio.OUT)
p = gpio.PWM(SERVO, 50)

good = [211, 200, 106, 217, 168]

def servoInit():
    print "servoInit"
    p.start(7.5)

def servoOn():
    print "servoOn"
    p.ChangeDutyCycle(4.5)

def servoNone():
    print "servoOn"
    p.ChangeDutyCycle(7.5)

def servoOff():
    print "servoOff"
    p.ChangeDutyCycle(10.5)

def clean():
    gpio.output(GREEN, False)
    gpio.output(RED, False)
    gpio.output(YELLOW, False)

def main():
    servoInit()
    while 1:
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        if status == MIFAREReader.MI_OK:
            (status, backData) = MIFAREReader.MFRC522_Anticoll()
            gpio.output(YELLOW, True)
            if status == MIFAREReader.MI_OK:
                mac = []
                for x in backData[0:-1]:
                    mac.append(hex(x).split('x')[1].upper())
                print ":".join(mac)
                if good == backData:
                    servoOn()
                    gpio.output(GREEN, True)
                    time.sleep(0.5)
                    servoNone()
                else:
                    gpio.output(RED, True)
                    servoOff()
                    time.sleep(0.5)
                    servoNone()
                time.sleep(1)
                gpio.output(YELLOW, False)
                gpio.output(RED, False)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        clean()
        MIFAREReader.GPIO_CLEEN()
        sys.exit(0)
