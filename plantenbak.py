import RPi.GPIO as GPIO
import time

pumpPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pumpPin, GPIO.OUT)


def activatePump(duration):
    print("Pump on.")
    GPIO.output(pumpPin, GPIO.HIGH)
    time.sleep(duration)
    print("pump off")
    GPIO.output(pumpPin, GPIO.LOW)


activatePump(10)
