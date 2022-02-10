import RPi.GPIO as GPIO
import os
import numpy as np


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.OUT)
GPIO.output(1, GPIO.LOW)
