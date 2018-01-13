#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

SleepTimeL = 3

try:
  GPIO.output(4, 0)
  print "TWO True"
  time.sleep(3);
  GPIO.output(4, 1)
  print "TWO False"
  time.sleep(3);

  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

