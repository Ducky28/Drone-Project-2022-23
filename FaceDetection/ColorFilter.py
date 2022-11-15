import cv2 as cv
import os
import numpy as np

cap = cv.VideoCapture(0)

while True: 
    cap = cv.VideoCapture(0)

    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    upperThreshold = np.array([180,255,255])
    lowerThreshold  = np.array([180,255,255])

    mask = cv.inRange(hsv, lowerThreshold, upperThreshold)
    result = cv.bitwise_and(frame, frame, mask = mask)
