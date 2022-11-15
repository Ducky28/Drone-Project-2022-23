import cv2 as cv
import numpy as np
import ColorFilter

#cap = cv.VideoCapture(0)
faceData = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret,frame = ColorFilter.getFilteredVideo()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    targets = faceData.detectMultiScale(gray, minSize=(10,10))

    amountFound = len(targets)

    if amountFound != 0:
        for(x, y, width, height) in targets:
            cv.rectangle(frame, (x, y), 
                      (x + height, y + width), 
                      (0, 255, 0), 5)
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()



