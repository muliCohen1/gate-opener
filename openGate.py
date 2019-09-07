__author__ = "Muli Cohen"

from bottle import route, run, template, #request - not needed at stripped down version. muliCohen
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
CONTROL_PIN = 18 #change on demand. muliCohen

@route('/') 
def index():
    return template('home.html')
    
@route('/on')
def index():
    GPIO.setup(CONTROL_PIN, GPIO.OUT)
    GPIO.output(CONTROL_PIN, False) #for supporting cheap chinese' relays. muliCohen
    time.sleep(2)    
    GPIO.setup(CONTROL_PIN, GPIO.IN) #for supporting reversed HIGH/LOW. muliCohen
    return template('home.html')

try: 
    run(host='0.0.0.0', port=80)
finally:  
    print('Cleaning up GPIO')
    GPIO.cleanup() #resets to input mode - important! muliCohen
