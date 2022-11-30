import serial
import numpy as np
import cv2 as cv

# gathering data from face detector file
centerCoords = ()

# creating arduino serial object
arduinoCommander = serial.Serial(port = "COM5", baudrate=19200, timeout=0.1)

def sendData(data):
    arduinoCommander.write(bytes(data, 'utf-8'))
    return data
