#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

print "Script starting..."

socket = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(socket,GPIO.OUT)

p = GPIO.PWM(socket,50)
p.start(7.5)

try:
	while True:
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		#p.ChangeDutyCycle(12.5)
		#time.sleep(1)
		#p.ChangeDutyCycle(2.5)
		#time.sleep(1)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
	print "Script complete."


