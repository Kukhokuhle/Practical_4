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
        for j in range(length):
            print(mylist[j])

# Under a rising-edge detection, regardless of current execution # callback function will be called
GPIO.add_event_detect(reset, GPIO.RISING, callback=callback1, bouncetime=200)
GPIO.add_event_detect(frequency, GPIO.RISING, callback=callback2, bouncetime=200)
GPIO.add_event_detect(stop, GPIO.RISING, callback=callback3, bouncetime=200)
GPIO.add_event_detect(display, GPIO.RISING, callback=callback4, bouncetime=200)
