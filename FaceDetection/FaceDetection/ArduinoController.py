import serial
import numpy as np
import cv2 as cv
import Constants

# gathering data from face detector file
centerCoords = ()

# creating arduino serial object
arduinoCommander = serial.Serial(port = Constants.COM_PORT_NAME, baudrate=Constants.RATE, timeout=Constants.TIMEOUT)

try:
    arduinoCommander.open()
except:
    pass


def sendData(data):
    arduinoCommander.write((data))
    print("Done fucked up")


