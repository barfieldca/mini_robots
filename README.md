# MyCobot - Raspberry Pi 4 Controller

The goal of these scripts is to create a method to manually control the MyCobot 280 M5 using the Rasberry Pi 4 as the robot controller. The controller is created using `pymycobot` Python module.

Author: Chandler Barfield

Organization: Virginia Commonwealth University - Dr. Shepherd's Research Team

## `MyCobot 280 M5 Setup`


To setup Elephant Robotics' MyCobot 280 M5, first, download MyStudio on a Windows/Linux/Mac machine. Afterwards, plug the machine into the MyCobot via the provided USB-C connection at he base port, open MyStudo and nagivate to the `Basic` tab on the left hand side. Now, download and flash `minirobot v2.1`. Next, unplug the machine from the base port and plug into the port located next to the LED display. Then, reopening MyStudio navigate back to the `Basic` tab and download and flash `AtomMain v6.1`.

Link to download MyStudio(https://www.elephantrobotics.com/en/downloads/)

## `Rasberry Pi 4 Information`
#### OS Version: Linix raspberrypi 5.10.52v71+

#### Python Version: 3.7.3

Download the `pymycobot` Python library to your Raspberry Pi. Then switch to the directory that the download is located in and type `sudo python3 setup.py install`

## `Circuit Design`

![circuitdia](https://user-images.githubusercontent.com/86315271/206774062-7a5913f9-0b00-45fc-b391-a0fd3c03b771.JPG)

Above is the cirucit designed on the breadboard, with their respective pin connections. Furthermore, a serial port connection between the Pi and MyCobot will need to be made using one of the available USB-A ports on the Raspberry Pi and the base USB-C on the MyCobot.
