#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)

SleepTimeL = 10

try:
  GPIO.output(17, 0)
  print "TWO True"
  time.sleep(2);
  GPIO.output(17, 1)
  print "TWO False"
  time.sleep(2);

  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

