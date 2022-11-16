import cv2 as cv
import numpy as np
import ColorFilter
import serial

cap = cv.VideoCapture(0)
faceData = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
centerCoords = ()

# creating arduino serial object
arduinoCommander = serial.Serial()
arduinoCommander.baudrate = 9600
arduinoCommander.port = 'COM5'
arduinoCommander.open() 

def getCenterCoords():
    return centerCoords

# print("REACHED THE FUCKING FILE")
if __name__ == '__main__':
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
            cv.rectangle(frame, (bigX, bigY), 
                        (bigX + bigHeight, bigY + bigWide), 
                        (0, 255, 0), 5)
            centerCoords = ((bigX+bigHeight)/2,(bigY+bigWide/2))
            print(centerCoords)
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()



