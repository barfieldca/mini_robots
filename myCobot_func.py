# myCobot Controller Functions.

# External Library Imports
from pymycobot import MyCobot, Angle, Coord
import RPi.GPIO as GPIO
import time
import serial
import os

def joint_sel(JOINT_ID):
    # Pin Definitions
    jntupPin = 19 # Joint up selector button pin 19.
    jntdownPin = 16 # Joint down selector button pin 16.

    joint = JOINT_ID # Program starts with joint 1 selected.

    # Pin Setup
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # Broadcom pin numbering scheme.
    GPIO.setup(jntupPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Set pin jntupPin to be an input pin and set inital value to be pulled high (on).
    GPIO.setup(jntdownPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Set pin jntdownPin to be an input pin and set inital value to be pulled high (on).

    previous_button_state1 = GPIO.input(jntupPin) # Setting previous_state for state_machine to detect clicks. 
    previous_button_state2 = GPIO.input(jntdownPin)
    
    print("Press Ctrl+C at anytime to return to the main menu...")

    try:
        while True:
        
            time.sleep(0.01) # Checks on 100Hz cycle.
            button_state1 = GPIO.input(jntupPin)
            button_state2 = GPIO.input(jntdownPin)
            
            if button_state1 != previous_button_state1 or button_state2 != previous_button_state2: # Code will only register a the switch from HIGH to LOW or LOW to HIGH.
                
                previous_button_state1 = button_state1 # Changes button states(state machine).
                previous_button_state2 = button_state2
                
                if button_state1 == GPIO.LOW and button_state2 == GPIO.HIGH: # Confirms only one button is pressed.
                    joint += 1
                    
                    if joint == 7:
                        joint = 1

                    print("Joint ID is now: ", joint)
                    
                elif button_state1 == GPIO.HIGH and button_state2 == GPIO.LOW: # Confirms only one button is pressed.
                    joint -= 1
                    
                    if joint == 0:
                        joint = 6
 
                    print("Joint ID is now: ", joint)
                else:
                
                    joint = joint
                    

    except KeyboardInterrupt:
        
        print("\nReturning to Main Menu...\n")
        GPIO.cleanup()
        return joint
        pass

      
# Code found https://www.jarutex.com/index.php/2022/01/06/9253/
def port_find():

    s = serial.Serial()
    portNames = [
        "/dev/ttyUSB0", # List of avaliable ports on Linux.
        "/dev/ttyUSB1",
        "/dev/ttyUSB2",
        "/dev/ttyUSB3",
        "/dev/ttyACM0",
        "/dev/ttyACM1",
        "/dev/ttyACM2",
        "/dev/ttyACM3"
    ]
    for pname in portNames:
        try: # Checks for valid connection.
            s.port = pname 
            s.open()
            if s.isOpen():
                return pname
                
        except: # If no valid connection is found passes back to myCobot.py.
            pass
            
    os.system('clear')
    print("Please check connection to myCobot, exiting Program...")
    time.sleep(1)
    exit()


def return_home(mc):
    
    mc.send_angles([0 ,-16, -130, 136, 0, 0], 80)
    print("\nMyCobot returning to HOME position...")
    time.sleep(1.5)  
    os.system('clear')
    

def movement(mc, JOINT_ID):
    # Pin Setup
    rotateupPin = 21
    rotatedownPin = 20

    # Getting starting angles.
    angles = mc.get_angles()
    x = angles[JOINT_ID - 1]

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # Broadcom pin numbering scheme.
    GPIO.setup(rotateupPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Set pin rotateupPin to be an input pin and set inital value to be pulled high (on).
    GPIO.setup(rotatedownPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Set pin rotatedownPin to be an input pin and set inital value to be pulled high (on).


    previous_button_state1 = GPIO.input(rotateupPin) # Setting previous_state for state_machine to detect clicks. 
    previous_button_state2 = GPIO.input(rotatedownPin)
    
    print("Press Ctrl+C at anytime to return to the main menu...")

    try:
        while True:
            
            time.sleep(0.01) # Checks on 100Hz cycle.
            button_state1 = GPIO.input(rotateupPin)
            button_state2 = GPIO.input(rotatedownPin)

            
            if button_state1 != previous_button_state1 or button_state2 != previous_button_state2: # Code will only register a the switch from HIGH to LOW or LOW to HIGH.
                    
                    previous_button_state1 = button_state1 # Changes button states(state machine).
                    previous_button_state2 = button_state2
                    
                    if button_state1 == GPIO.LOW and button_state2 == GPIO.HIGH: # Confirms only one button is pressed.
                        
                        if JOINT_ID == 1:
                            x += 3
                            mc.send_angle(Angle.J1.value, x, 80)
                        elif JOINT_ID == 2:
                            x += 3
                            mc.send_angle(Angle.J2.value, x, 80)
                        elif JOINT_ID == 3:
                            x += 3
                            mc.send_angle(Angle.J3.value, x, 80)    
                        elif JOINT_ID == 4:
                            x += 3
                            mc.send_angle(Angle.J4.value, x, 80)
                        elif JOINT_ID == 5:
                            x += 3
                            mc.send_angle(Angle.J5.value, x, 80)
                        elif JOINT_ID == 6:
                            x += 3
                            mc.send_angle(Angle.J6.value, x, 80)
                        else:
                            raise Exception(print("ERR: Could not detect JOINT_ID"))
                        
                    elif button_state1 == GPIO.HIGH and button_state2 == GPIO.LOW: # Confirms only one button is pressed.
                        
                        if JOINT_ID == 1:
                            x -= 3
                            mc.send_angle(Angle.J1.value, x, 80)
                        elif JOINT_ID == 2:
                            x -= 3
                            mc.send_angle(Angle.J2.value, x, 80)
                        elif JOINT_ID == 3:
                            x -= 3
                            mc.send_angle(Angle.J3.value, x, 80)    
                        elif JOINT_ID == 4:
                            x -= 3
                            mc.send_angle(Angle.J4.value, x, 80)
                        elif JOINT_ID == 5:
                            x -= 3
                            mc.send_angle(Angle.J5.value, x, 80)
                        elif JOINT_ID == 6:
                            x -= 3
                            mc.send_angle(Angle.J6.value, x, 80)
                        else:
                            raise Exception(print("ERR: Could not detect JOINT_ID"))

    except KeyboardInterrupt:
    
        print("\nReturning to Main Menu...\n")
        GPIO.cleanup()
        os.system('clear')