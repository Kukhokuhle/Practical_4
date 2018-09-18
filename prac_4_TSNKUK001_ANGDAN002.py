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

#initialise pull down resistors for buttons
GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(frequency, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(stop, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(display, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Define delay between readings
delay = 0.5   #default delay is 500 ms = 0.5 s

# define our clear function for clearing the console
def clear():
    _ = system('clear')

# function definition: threaded callback
def callback1(reset): #resets timer and clears console
    global start_time
    start_time = time.time()
    
    clear()


def callback2(frequency):
    global delay
    if delay == 2:
            delay = 0.5
    elif delay == 1:
            delay = 2
    elif delay == 0.5:
            delay = 1

def callback3(stop):
    global go
    if go == True:
            go = False
    else:
            go = True


def callback4(display):
    global mylist
    length = len(mylist)  #length of list
        print("Time           Timer      Pot       Temp      Light")
        if length > 4:
            for i in range(5):
                print(mylist[i])
        else:
            or j in range(length):
                print(mylist[j])

