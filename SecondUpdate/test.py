import cv2
import face_recognition
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import pickle
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(X, GPIO.OUT)

nameDefault = "unknown"
autoFile = "encodings.pickle"

imgs = pickle.loads(open(autoFile, "rb").read())

vid = VideoStream(src=0,framerate=30).start()
time.sleep(1.0)
capture = FPS().start()

        
while True:
        
    frame = vid.read()
    frame = imutils.resize(frame, width=600)
    facialDet = face_recognition.face_locations(frame)
    encodings = face_recognition.face_encodings(frame, facialDet)
    personsNames = []

    for encoding in encodings:

        owner = face_recognition.compare_faces(imgs["encodings"], encoding)
        personsNames = "Unknown"
        
        if True in owner:
            ownerIndex = [i for (i, b) in enumerate(owner) if b]
            faceCount = {}
       
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
vid.release()
cv2.destroyAllWindows()
