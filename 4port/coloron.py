#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT)

try:
   GPIO.output(22, False)

# End program cleanly with keyboard
except KeyboardInterrupt:
#  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

