#!/usr/bin/env python


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)

SleepTimeL = 10


GPIO.output(22, True)
print "FOUR True"
time.sleep(SleepTimeL);
GPIO.output(22, False)
print "FOUR False"
time.sleep(SleepTimeL);

GPIO.cleanup()
print "Good bye!"

