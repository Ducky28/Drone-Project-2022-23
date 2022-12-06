import serial
import numpy as np
import cv2 as cv
import Constants
import time

# gathering data from face detector file
centerCoords = ()

# creating arduino serial object
arduinoCommander = serial.Serial(port = Constants.COM_PORT_NAME, baudrate=Constants.RATE, timeout=Constants.TIMEOUT)

try:
    arduinoCommander.open()
except:
    pass

def chooseAction(XCoord, YCoord):
    if(abs(XCoord - Constants.X_MID) <= 5 and abs(YCoord - Constants.y_MID) <= 5):
        time.wait(5)
        sendCommand("SPIN MOTORS")
        if(abs(XCoord - Constants.X_MID) <= 5 and abs(YCoord - Constants.y_MID) <= 5):
            sendCommand("FIRE")
        else:
            sendCommand("STOP")
        

def sendCommand(command):
    arduinoCommander.write((command))
    print("SENT COMMAND: " + command)


