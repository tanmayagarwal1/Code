from dronekit import connect,VehicleMode, LocationGlobalRelative 
from pymavlink import mavutil 
import argparse
import serial 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
parser= argparse.ArgumentParser()
parser.add_argument('--connect',default='127.0.0.1:14550')
args=parser.parse_args()
print("connecting to vehicle")
vehicle=connect(args.connect, baud=921600,wait_ready=True )
ser=serial.Serial("/dev/ttyACM0",9600,timeout=1)
print(" Armed: %s" % vehicle.armed)

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

if __name__=='__main__':
	try:
		while True:
			dist=distance(22,25)
			if dist<45:
				vehicle.channels.overrides['2'] = 1600
				time.sleep(0.3)
				vehicle.channels.overrides['2']=0 
			else:
				vehicle.channels.overrides['2']=0 
				

	except KeyboardInterrupt:
		print("stopped")
		vehicle.close()
		GPIO.cleanup
				