#!/usr/bin/env python
# This script gets weather data from smhi and turns on a LED
# if the forecast expects any rainfall/snowfall within the next 8 hours.
import requests, json, time
from pprint import pprint
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

red_gpio = 12
green_gpio = 16
GPIO.setup(red_gpio, GPIO.OUT)
GPIO.setup(green_gpio, GPIO.OUT)

lund_latitude = 55.71
lund_longitude = 13.19

time_now = datetime.now()

r = requests.get('http://opendata-download-metfcst.smhi.se/api/category/pmp1.5g/version/1/geopoint/lat/' +
                 str(lund_latitude) +
                 '/lon/' +
                 str(lund_longitude) +
                 '/data.json')
# pprint(r.json())

# Controls the json object and return true/false depending on weather *fall.
def any_downfall(r):
    time_now_as_string = "%d-%d-%dT%d:00:00Z" % (datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour)
    data = json.loads(r.text)
    start_index = 0
    for x in range(0, len(data["timeseries"])) :
        if (data["timeseries"][x]["validTime"] == time_now_as_string):
            start_index = x
            break

    for x in range(start_index, start_index + 8):
        if (data["timeseries"][x]["pcat"] != 0):
            # Rain- or snow-fall
            return True
        
    return False;

# Turns on/off red LED
def red_led_on( status ):
    GPIO.output(red_gpio, status)
    
# Turns on/off green LED
def green_led_on( status ):
    GPIO.output(green_gpio, status)

def blinkblink():
    green_led_on(True)
    red_led_on(True)
    time.sleep(1)
    green_led_on(False)
    red_led_on(False)
    time.sleep(0.5)
    green_led_on(True)
    time.sleep(0.5)
    red_led_on(True)
    time.sleep(0.5)
    green_led_on(False)
    time.sleep(0.5)
    red_led_on(False)
    time.sleep(0.5)
    green_led_on(True)
    time.sleep(0.5)
    red_led_on(True)
    time.sleep(0.5)
    green_led_on(False)
    time.sleep(0.5)
    red_led_on(False)
    time.sleep(0.5)
    red_led_on(True)
    green_led_on(True)
    time.sleep(0.3)
    red_led_on(False)
    green_led_on(False)
    time.sleep(1)

# ====================== End of Functions =====================

blinkblink()

rain_or_snow = any_downfall(r)
if rain_or_snow:
    red_led_on(True)
    green_led_on(False)
else :
    red_led_on(False)
    green_led_on(True)
    



