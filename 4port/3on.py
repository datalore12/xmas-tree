#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)

SleepTimeL = 3

try:
  GPIO.output(27, 0)
  print "FOUR True"
  time.sleep(SleepTimeL);
  GPIO.output(27, 1)
  print "FOUR False"
  time.sleep(SleepTimeL);

  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

