#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)

SleepTimeL = 2

try:
  GPIO.output(22, 0)
  print "FOUR True"
  time.sleep(SleepTimeL);
  GPIO.output(22, 1)
  print "FOUR False"
  time.sleep(SleepTimeL);

  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

