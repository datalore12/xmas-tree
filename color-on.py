#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinlist = [22]

for i in pinlist:
  GPIO.setup(i, GPIO.OUT)

SleepTimeL = 2

try:
  GPIO.output(22, False)

# End program cleanly with keyboard
except KeyboardInterrupt:
#  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

