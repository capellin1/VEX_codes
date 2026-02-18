#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
right_drive_smart = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)


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
drivetrain_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_needs_to_be_stopped_controller_1, controller_1_up_down_buttons_control_motors_stopped, controller_1_x_b_buttons_control_motors_stopped, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis2 + axis1
            # right = axis2 - axis1
            drivetrain_left_side_speed = controller_1.axis2.position() + controller_1.axis1.position()
            drivetrain_right_side_speed = controller_1.axis2.position() - controller_1.axis1.position()
            
            # check if the values are inside of the deadband range
            if abs(drivetrain_left_side_speed) < 5 and abs(drivetrain_right_side_speed) < 5:
                # check if the motors have already been stopped
                if drivetrain_needs_to_be_stopped_controller_1:
                    # stop the drive motors
                    left_drive_smart.stop()
                    right_drive_smart.stop()
                    # tell the code that the motors have been stopped
                    drivetrain_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the motors next
                # time the input is in the deadband range
                drivetrain_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
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
remote_control_code_enabled = False

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration
#start code

import math
drivetrain.drive(FORWARD)
drivetrain.turn(RIGHT)
posx=0
posy = 0
direction=0
def get_controller_1():
    global posx
    global posy
    global direction
    ax2=controller_1.axis1.position()
    ax1=controller_1.axis2.position()
    drivetrain.set_drive_velocity(ax1, PERCENT)
    drivetrain.set_turn_velocity(ax2, PERCENT)
    if ax2 is not 0:
        drivetrain.turn(LEFT)
    drivetrain.drive(FORWARD)
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
        controller_1.screen.print("x:",posx,"y:",posy)
drivetrain.set_drive_velocity(0, PERCENT)
drivetrain.set_turn_velocity(0, PERCENT)


controller_1.screen.set_cursor(1, 1)
while True:
    get_controller_1()


