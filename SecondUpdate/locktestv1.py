import RPi.GPIO as GPIO
import os
import numpy as np
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

GPIO.output(27, GPIO.LOW)

time.sleep(1)

GPIO.output(27, GPIO.HIGH)

time.sleep(1)

GPIO.output(27, GPIO.LOW)

time.sleep(1)

GPIO.cleanup()