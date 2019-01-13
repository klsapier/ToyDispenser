#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

print "Open cycle starting..."

socket = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(socket,GPIO.OUT)

p = GPIO.PWM(socket,50)
p.start(7.5)

#Open
p.ChangeDutyCycle(12.5)
time.sleep(1)

p.stop()
GPIO.cleanup()
print "Open cycle complete."


