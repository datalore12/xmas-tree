#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinlist = [4, 17, 27, 22]

for i in pinlist:
  GPIO.setup(i, GPIO.OUT)

SleepTimeL = 2

try:
  GPIO.output(4, False)
  GPIO.output(17, False)
  GPIO.output(27, False)
  GPIO.output(22, False)

# End program cleanly with keyboard
except KeyboardInterrupt:
#  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

