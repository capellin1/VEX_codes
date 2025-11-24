
#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code

# Define Drivetrain Motors
# Assuming Left Motor is connected to PORT1 and Right Motor to PORT10
# Note: The polarity (True/False) may need to be adjusted based on your robot's wiring to ensure both sides spin FORWARD together.
left_motor = Motor(Ports.PORT1, True) # Configure polarity if necessary
right_motor = Motor(Ports.PORT10, False)

# Define the Controller
controller_1 = Controller(PRIMARY) # Ensures the controller is initialized [13]

# Pre-Autonomous Function
def pre_autonomous():
    # Used for any setup your robot may need (e.g., calibrating sensors, setting variables) [14].
    
    # Example: Setting default velocity for the motors (optional) [15].
    left_motor.set_velocity(50, PERCENT)
    right_motor.set_velocity(50, PERCENT)
    
    # Example: Calibrating an Inertial Sensor (if Dex has one) [16].
    # gyro.calibrate()
    pass 
# Autonomous Mode Function (Pre-programmed moves)
def autonomous():
    # Commands within this function run when the match begins the Autonomous period [9].
    
    # Example Move 1: Drive Forward 200 mm [17, 18]
    # Note: This command assumes a Drivetrain device named 'drivetrain' is configured.
    drivetrain.drive_for(FORWARD, 200, MM)
    
    # Example Move 2: Wait 1 second [17]
    wait(1, SECONDS) 
    
    # Example Move 3: Drive in Reverse 100 mm [19]
    drivetrain.drive_for(REVERSE, 100, MM)
    
    # Example Move 4: Turn Right 90 degrees [20]
    # drivetrain.turn_for(RIGHT, 90, DEGREES)
# Driver Control Function (Controller control)
def user_control():
    # Commands within this function run during the driver control portion of a VRC match [9].
    
    # The while True loop ensures the robot constantly responds to controller input [7, 10].
    while True:
        # Use Tank Drive control:
        # Left Joystick (Axis 3) controls the Left Motor velocity.
        # Right Joystick (Axis 2) controls the Right Motor velocity [6, 7].
        
        # 1. Set the velocity of the motors based on the controller joystick positions (0-100 PERCENT)
        left_motor.set_velocity(controller_1.axis3.position(), PERCENT) [6]
        right_motor.set_velocity(controller_1.axis2.position(), PERCENT) [6]
        
        # 2. Spin the motors continuously in the forward direction. 
        # The velocity set above determines the actual speed and direction (positive velocity for FORWARD, negative for REVERSE) [6, 7, 11].
        left_motor.spin(FORWARD) [6]
        right_motor.spin(FORWARD) [6]
        
        # 3. Wait a short duration (5 milliseconds is standard for VEX control loops) [7].
        wait(5, MSEC) 


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

myVariable = 0

def when_started1():
    global myVariable
    pass
  # Turn to the right for 400 degrees.
drivetrain.turn_for(RIGHT, 400, DEGREES)
# Print the V5 Robot's current angle of rotation.
brain.screen.print(drivetrain.rotation(DEGREES))


when_started1()
