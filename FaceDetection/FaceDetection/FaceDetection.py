import cv2 as cv
import numpy as np
import ColorFilter
import serial
import ArduinoController

cap = cv.VideoCapture(0)
faceData = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# print("REACHED THE FUCKING FILE")
while True:
    ret,frame = cap.read()
    # print("reached initial frame read")
    frame = ColorFilter.filterFace(frame)
    # print("gathered frame from color filter")
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # print("reached greyscale stage")
    targets = faceData.detectMultiScale(gray, minSize=(10,10))

    amountFound = len(targets)

    if amountFound != 0:
        biggestFaceNum = 0
        bigX = 0
        bigY = 0
        bigWide = 0
        bigHeight = 0
        for(x, y, width, height) in targets:
            if x+y+width+height > biggestFaceNum:
                biggestFaceNum = x+y+width+height
                bigX = x
                bigY = y
                bigWide = width
                bigHeight = height
        centerCoords = ((bigX+bigHeight)/2,(bigY+bigWide/2))
        xCoord = str(centerCoords[0])
        yCoord = str(centerCoords[1])
        sendableData = xCoord + "," + yCoord
        print(ArduinoController.sendData(sendableData))
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()



