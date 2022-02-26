import cv2, os
import numpy
import face_recognition
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(X, GPIO.OUT)

from testlink import TestLink
vid = cv2.VideoCapture(0)
extFacial = TestLink()

while True:
    
    
    ret, frame = vid.read()
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
vid.release()
cv2.destroyAllWindows()