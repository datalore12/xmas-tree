# Install the Python Requests library:
# `pip install requests`

from flask import Flask
app = Flask(__name__)
import RPi.GPIO as GPIO
import time
import random
import threading


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

@app.route('/allon')
def allon():
    pinlist = [4, 17, 27, 22]

    for i in pinlist:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)

    event.clear()
    event.set()

    try:
      GPIO.output(4, False)
      GPIO.output(17, False)
      GPIO.output(27, False)

    # End program cleanly with keyboard
    except KeyboardInterrupt:
     #print "  Quit"

      # Reset GPIO settings
      GPIO.cleanup()
      return "Hello World from Flask"


@app.route('/coloron')
def coloron():

    pinlist = [4, 17, 27, 22]

    for i in pinlist:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)


    try:
      GPIO.output(22, False)

    # End program cleanly with keyboard
    except KeyboardInterrupt:
     #print "  Quit"

      # Reset GPIO settings
      GPIO.cleanup()
      return "Hello World from Flask"

@app.route('/alloff')
def allof():
    pinlist = [4, 17, 27, 22]

    for i in pinlist:
      GPIO.setup(i, GPIO.OUT)

    SleepTimeL = 2

    try:
      GPIO.output(4, True)
      GPIO.output(17, True)
      GPIO.output(27, True)
      GPIO.output(22, True)

    # End program cleanly with keyboard
    except KeyboardInterrupt:
    # print "  Quit"

      # Reset GPIO settings
      GPIO.cleanup()

      return "Hello World from Flask"

@app.route('/flash')
def flash():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  pinList = [4, 17, 27, 22]
  SleepTimeL = 1

  for i in pinList:
      GPIO.setup(i, GPIO.OUT)
      GPIO.output(i, GPIO.LOW)

  event.clear()
  event.set()
  while event.is_set():
    b = random.choice(pinList)
    GPIO.output(b, GPIO.HIGH)
    time.sleep(SleepTimeL);

    GPIO.output(b, GPIO.LOW)
    time.sleep(SleepTimeL);


event = threading.Event()
t1 = threading.Thread(target = flash)
t2 = threading.Thread(target = allon)

t1.start
t2.start

if __name__ == '__main__':
    port = 8550 #the custom port you want
    app.run(host='0.0.0.0', port=port)
