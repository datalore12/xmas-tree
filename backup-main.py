# Install the Python Requests library:
# `pip install requests`

from flask import Flask
app = Flask(__name__)
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

@app.route('/allon')
def allon():
    pinlist = [4, 17, 27]

    for i in pinlist:
        GPIO.setup(i, GPIO.OUT)

    SleepTimeL = 2

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
    
    pinlist = [22]

    for i in pinlist:
        GPIO.setup(i, GPIO.OUT)

    SleepTimeL = 2

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


if __name__ == '__main__':
    port = 8550 #the custom port you want
    app.run(host='0.0.0.0', port=port)
