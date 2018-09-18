#!/usr/bin/python
import spidev
import time
import os
import sys
import RPi.GPIO as GPIO
from datetime import datetime

# import only system from os
from os import system, name

#import pytz      #module pytz not found
#from pytz import timezone
# Open SPI bus


GPIO.setmode(GPIO.BCM) #specify numbering system

#attach the buttons to GPIO pins
reset = 4
frequency = 17
stop = 27
display = 22
