import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance(GPIO_TRIGGER,GPIO_ECHO):

    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
 
    TimeElapsed = StopTime - StartTime
 
    distance = (TimeElapsed * 34300) / 2
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance(18,24)
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()