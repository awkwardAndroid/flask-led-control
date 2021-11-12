import pyfirmata
import time, os, pathlib

board = pyfirmata.Arduino('COM4') # Serial port where the arduino uno is connected
path = pathlib.Path("state/") # Folder where the text file is whitch controls if the led is on or off

def read_state():
    value = os.listdir(path) # Get the filename in folder
    for item in value:
        if item == "0.txt":
            board.digital[13].write(0) # Turn led off
        elif item == "1.txt":
            board.digital[13].write(1) # Turn led on

while True:
    read_state()
    time.sleep(.5) # Small delay so the script doesnt run at the speed of 100 km/h
