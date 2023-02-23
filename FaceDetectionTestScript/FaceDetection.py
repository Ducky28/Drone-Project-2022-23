import cv2 as cv
import numpy as np
import serial

import ColorFilter

cap = cv.VideoCapture(0)
faceData = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

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
        bigX = bigY = bigWide = bigHeight = 0
        for(x, y, width, height) in targets:
            
            if x+y+width+height > biggestFaceNum:
                biggestFaceNum = x+y+width+height
                bigX, bigY, bigWide, bigHeight = x, y, width, height

        cv.rectangle(frame, (x, y), (bigX + bigWide, bigY + bigHeight), (0, 255, 0), 3)

        
        # attempting to display the frame breaks the code for some reason, will need to look into issue later

    if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
cv.destroyAllWindows()


