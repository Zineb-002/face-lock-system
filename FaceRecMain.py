import cv2
import numpy as np
import face_recognition
import os
import RPi.GPIO as GPIO
import time


RELAY = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)
GPIO.output(RELAY, GPIO.LOW)

doorUnlock = False
path = 'img'
images = []
name = []
myList = os.listdir(path)
print(myList)

if len(myList) == 0:
    print("Face_Images folder is Empty, please add some photo")
else:
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        name.append(os.path.splitext(cl)[0])
    print(name)

def drawRectangelWithName(ParsonName):
    print(ParsonName)
    y1, x2, y2, x1 = faceLoc
    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.rectangle(img, (x1, y2 - 55), (x2, y2), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, ParsonName, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)






def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture('http://192.168.100.55/mjpeg/1')

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        print("here")
        if matches[matchIndex]:
            namePerson = name[matchIndex].upper()
            drawRectangelWithName(namePerson)

            GPIO.output(RELAY,GPIO.HIGH)
            prevTime = time.time()
            doorUnlock = True
            print("Door Unlocked")
        else:
            drawRectangelWithName("Unknown")
            print("No match")


    cv2.imshow('webcam', img)
    cv2.waitKey(1)

    if doorUnlock == True and time.time() - prevTime > 5:
        doorUnlock = False
        GPIO.output(RELAY, GPIO.LOW)
        print("Door Locked")
