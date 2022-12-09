# myCobot Controller Interface Design.
from pymycobot import MyCobot
from myCobot_func import *
import os
import time

# Robot Connection/Setup Starts Here.
JOINT_ID = 1 # Starting ID for joint.
BAUDRATE = 115200 # Baudrate for serial port data transfer.
PORT_ID = port_find() # Grabs Port ID and stores it here.
mc = MyCobot(PORT_ID, BAUDRATE)
print("MyCobot is now active.\n\n")
time.sleep(5) # For best results, wait for 5s after connecting to serial port.
mc.send_angles([0 ,-16, -130, 136, 0, 0], 80)
os.system('clear')

# Main Menu Setup Starts Here.

try:
    while True:
        print("Controller Menu...\n") # Main Interface to cycle through controller abilities. 
        print("1.  Change Joint ID")
        print("2.  Return to Home Position")
        print("3.  Jog Robot")
        print("Ctrl+C.  Exit Program...")
        sel = int(input())

        if sel == 1:
            print("Current Joint ID: ", JOINT_ID)
            JOINT_ID = joint_sel(JOINT_ID) # Function call to change the joint ID using the button interface. 
            
            time.sleep(1) # Program waits 1 second then clears the console and returns to the main menu.
            os.system('clear')
            print("New Joint ID: ", JOINT_ID)
        elif sel == 2:
            return_home(mc)
        elif sel == 3:
            movement(mc, JOINT_ID)

except KeyboardInterrupt:
    
    os.system('clear')
    print("Exiting Program...")
    time.sleep(1)
    
# https://pypi.org/project/pymycobot/