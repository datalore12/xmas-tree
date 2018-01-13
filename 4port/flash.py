#!/usr/bin/env python
import random
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = [4, 17, 27, 22]
SleepTimeL = 1

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

try:
	while True:
		b = random.choice(pinList) 
		GPIO.output(b, GPIO.HIGH)
		time.sleep(SleepTimeL);

		GPIO.output(b, GPIO.LOW)
		time.sleep(SleepTimeL);

except KeyboardInterrupt:
	GPIO.cleanup()
