#!/usr/bin/env python
# Turns on red and green LEDS. These LEDs is used by the weather.py program.
# This script is used for testing mostly.

import RPi.GPIO as GPIO

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
    
