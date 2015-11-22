#!/usr/bin/env python
# Blinks the led
# This script is used for testing mostly.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

red_gpio = 12
green_gpio = 16
GPIO.setup(red_gpio, GPIO.OUT)
GPIO.setup(green_gpio, GPIO.OUT)


# Turns on/off red LED
def red_led_on( status ):
    GPIO.output(red_gpio, status)
    
# Turns on/off green LED
def green_led_on( status ):
    GPIO.output(green_gpio, status)

# ====================== End of Functions =====================

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

GPIO.cleanup()



