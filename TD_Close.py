#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

print "Close cycle starting..."

socket = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(socket,GPIO.OUT)

p = GPIO.PWM(socket,50)
p.start(7.5)

#Close
p.ChangeDutyCycle(7.5)
time.sleep(1)

p.stop()
GPIO.cleanup()
print "Close cycle complete."


