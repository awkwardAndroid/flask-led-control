# flask-led-control
A simple program to control a led using Arduino uno and python.
If you want to try this, I assume that you aren't a noob and know how to Google things.

I made this project in a few hours so this code is pretty shit. I just wanted to test how to control the led with python.
This program is tested with windows 11 and I'm not sure if it will work with mac or linux.
### How the program works?
#### Controller.py
```
This script looks at the folder "state" and looks at the file's name in there.
If the filename is "0.txt" the led is off or will turn off.
And if its "1.txt" the led is or will turn on.
```

#### config.py
```
This will create the local flask server whitch is used to control the leds state.
On the index page you see the leds current state and can use the two buttons to turn the led on or off.
When you press either of the buttons, the program renames the text file in the "state" folder and depending on the button,
it will rename the file to "0.txt" or "1.txt".
```

ps. this is not a full tutorial.

### Items used:
* Arduino uno
* Resistor
* Led
* Wires
* Breadboard

### Arduino uno setup
[Download arduino app](https://www.arduino.cc/en/software)
1. Connect Arduino to pc
2. Open Arduino IDE
3. Setup & check port -> Tools -> Port (My was "COM4")
4. Click -> File -> Examples -> Firmata -> StandardFirmata
5. Upload to Arduino uno

### Breadboard setup
* Connect pin 13 to -> resistor -> led
* Connect GND(Ground) to the end of the led
* Thats it

### Python external modules used
* [Flask](https://pypi.org/project/Flask/)
* [pyfirmata](https://pypi.org/project/pyFirmata/)


Download the code and the things you probably have to change are:

> from controller.py -> line 4
```python
board = pyfirmata.Arduino('COM4') # Serial port where the arduino uno is connected
```
> from config.py -> line 58.
```python
subprocess.call("start python controller.py", shell=True)
```
^ This works with windows, but haven't tested with linux.

#### To run the program, just run config.py
