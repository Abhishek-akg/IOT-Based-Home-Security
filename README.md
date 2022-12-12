# IOT-Based-Home-Security
## Overview

Project for Internet of Things and Design CS G518 on BITS Pilani, Goa Campus

## Hardware Requirements

This project requires a Raspberry pi, a camera module, mouse, keyboard, monitor, HDMI cable, breadboard, 2 LED lights, 2 resistors and connecting wires.

## Software Requirements and Dependencies

Python should be installed on the Raspberry pi

Verify if you have python installed first (if not, install it):
```
$ python -V
```

The following packages should also be installed
```
$ pip install numpy
$ pip install dlib
$ pip install face_recognition
$ pip install opencv2
$ pip install pillow
$ sudo apt-get install python-rpi.gpio python3-rpi.gpio
```

Now to run the program
```
$ python face_recog.py
```

Now the raspberry pi works as a home security system where it will open the door when it matches with a known face.
To train the model for more faces or some another face one can do so by refering to line 16 or 19 of the face_recog.py file.
One can remove the GPIO codes if they don't want to blink particular lights from pin 37 and 3 of raspberry pi when a known or unknown face is detected.
