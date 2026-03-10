#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_36_1, False)
motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_36_1, False)
controller_1 = Controller(PRIMARY)
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_36_1, True)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_36_1, False)


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



# define variables used for controlling motors based on controller inputs
controller_1_up_down_buttons_control_motors_stopped = True
controller_1_x_b_buttons_control_motors_stopped = True

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global controller_1_up_down_buttons_control_motors_stopped, controller_1_x_b_buttons_control_motors_stopped, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            # check the buttonUp/buttonDown status
            # to control motor_4
            if controller_1.buttonUp.pressing():
                motor_4.spin(FORWARD)
                controller_1_up_down_buttons_control_motors_stopped = False
            elif controller_1.buttonDown.pressing():
                motor_4.spin(REVERSE)
                controller_1_up_down_buttons_control_motors_stopped = False
            elif not controller_1_up_down_buttons_control_motors_stopped:
                motor_4.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_up_down_buttons_control_motors_stopped = True
            # check the buttonX/buttonB status
            # to control motor_3
            if controller_1.buttonX.pressing():
                motor_3.spin(FORWARD)
                controller_1_x_b_buttons_control_motors_stopped = False
            elif controller_1.buttonB.pressing():
                motor_3.spin(REVERSE)
                controller_1_x_b_buttons_control_motors_stopped = False
            elif not controller_1_x_b_buttons_control_motors_stopped:
                motor_3.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_x_b_buttons_control_motors_stopped = True
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration
#start code

import math
motor_1.spin(FORWARD)
motor_2.spin(FORWARD)
posx=0
posy = 0
direction=0
def get_controller_1():
    global posx
    global posy
    global direction
    ax2=controller_1.axis1.position()
    ax1=controller_1.axis2.position()
    motor_1.set_velocity(ax1-(ax2*0.5), PERCENT)
    motor_2.set_velocity(ax1+(ax2*0.5), PERCENT)
    if controller_1.buttonA.pressing():
        motor_3.spin(FORWARD)
    elif controller_1.buttonB.pressing():
        motor_3.spin(REVERSE)
    else:
        motor_3.stop()
    if controller_1.buttonX.pressing():
        motor_4.spin(FORWARD)
    elif controller_1.buttonY.pressing():
        motor_4.spin(REVERSE)
    else:
        motor_4.stop()
    if brain.timer.time(MSEC)%200 == 0:
        direction+=ax1
        posx+=ax1*math.cos(ax2)
        posy+=ax1*math.sin(ax2)
        controller_1.screen.clear_row(1)
        controller_1.screen.set_cursor(1, 1)
        controller_1.screen.print("x:",ax1,"y:",ax2)
motor_1.set_velocity(0, PERCENT)
motor_2.set_velocity(0, PERCENT)


controller_1.screen.set_cursor(1, 1)
while True:
    get_controller_1()


