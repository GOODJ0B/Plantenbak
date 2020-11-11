import RPi.GPIO as GPIO
import time

pumpPin = 18
sensorPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pumpPin, GPIO.OUT)
GPIO.setup(sensorPin, GPIO.IN)

def activatePump(duration):
    print("Pump on.")
    GPIO.output(pumpPin, GPIO.LOW)
    for i in range(10):
       print(str(GPIO.input(sensorPin)))
       time.sleep(duration / 10)
    print("pump off")
    GPIO.output(pumpPin, GPIO.HIGH)


activatePump(10)

while True:
    print(str(GPIO.input(sensorPin)))
    time.sleep(1)