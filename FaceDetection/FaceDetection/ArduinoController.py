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

# chooses action based on center of target distance from centerpoint of screen

def chooseAction(XCoord, YCoord):
    if(abs(XCoord - Constants.X_MID) <= 1000 and abs(YCoord - Constants.Y_MID) <= 1000):
        sendCommand("SPIN MOTORS")
        print("LOCKING")
        time.sleep(5)
        if(abs(XCoord - Constants.X_MID) <= 1000 and abs(YCoord - Constants.Y_MID) <= 1000):
            sendCommand("FIRE")
            sendCommand("RELOAD")
        else:
            sendCommand("STOP")
        
# Encodes string command and writes it to arduino via serial port

def sendCommand(command):
    arduinoCommander.write(command.encode('utf-8'))
    print("SENT COMMAND: " + command)


