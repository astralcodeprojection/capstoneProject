import face_recognition
import cv2
import os
import numpy as nmpy

class TestLink:
   
    
    def initial(facials):
        
        currentOwner = face_recognition.load_image_file('home/pi/facials/photos/*PHOTOHERE*')
        COencode = face_recognition.face_encodings(currentOwner)[0]
        
        facial_encoded = [COencode]
        encodedArrayNames = ["Owner"]
        
    