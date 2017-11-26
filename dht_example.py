#!/usr/bin/python
import RPi.GPIO as GPIO
import dht
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using pin 14

def doit(obj, retry=5000, file='/tmp/dht22'):
	for x in range(0, retry):
		result = obj.read()
		if result.is_valid():
			cas=str(datetime.datetime.now())[:16]
			f = open(file, 'a')
			#print("pokus c.: " + str(x))
			values = (str(cas) + ", " + str(result.temperature) + ", " + str(result.humidity) + "\n")
			f.write(values)
			f.close()
			break

instance = dht11.DHT11(pin=5, sensor="DHT22")
instance1 = dht11.DHT11(pin=7, sensor="DHT22")
doit(file='/home/sensor/th.csv', obj=instance)
doit(file='/home/sensor/th1.csv', obj=instance1)
