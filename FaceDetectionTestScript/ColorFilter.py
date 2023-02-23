import cv2 as cv
import os
import numpy as np

cap = cv.VideoCapture(0)


lowerColor = [0, 0, 0]
upperColor = [255, 255, 255]

def  changeColor(val, color, bound):
    if bound:
        upperColor[color] = val
    else:
        lowerColor[color] = val

cap = cv.VideoCapture(0)

#cv.namedWindow('ColorTracking')

#cv.createTrackbar('Lower R', 'ColorTracking', 0, 255, lambda n: changeColor(n, 0, False))
#cv.createTrackbar('Lower G', 'ColorTracking', 90, 255, lambda n: changeColor(n, 1, False))
#cv.createTrackbar('Lower B', 'ColorTracking', 111, 255, lambda n: changeColor(n, 2, False))

#cv.createTrackbar('Upper R', 'ColorTracking', 204, 255, lambda n: changeColor(n, 0, True))
#cv.createTrackbar('Upper G', 'ColorTracking', 206, 255,  lambda n: changeColor(n, 1, True))
#cv.createTrackbar('Upper B', 'ColorTracking', 255, 255,  lambda n: changeColor(n, 2, True))

       
def filterFace(frame):
    lowerColor = [0, 18, 7]
    upperColor = [87, 140, 255]

    into_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_limit = np.array(lowerColor)
    upper_limit = np.array(upperColor)
    
    b_mask=cv.inRange(into_hsv,lower_limit,upper_limit)
    red=cv.bitwise_and(frame,frame,mask=b_mask)
    return red


if __name__ == "__main__":
    while True:
        ret, frame = cap.read()
        into_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        lower_limit = np.array(lowerColor)
        upper_limit = np.array(upperColor)
            
        b_mask=cv.inRange(into_hsv,lower_limit,upper_limit)
        red=cv.bitwise_and(frame,frame,mask=b_mask)
    
        cv.imshow("ColorTracking", red)
        cv.waitKey(1)

