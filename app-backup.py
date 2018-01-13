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
    # No Shut Interface
    # DELETE http://nso:8080/api/running/devices/device/p1/config/cisco-ios-xr:interface/GigabitEthernet/0%2F0%2F0%2F2/shutdown
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
#      print "  Quit"

      # Reset GPIO settings
      GPIO.cleanup()

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

        

if __name__ == '__main__':
    port = 8000 #the custom port you want
    app.run(host='0.0.0.0', port=port)
