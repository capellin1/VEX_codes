import math
drivetrain.drive(FORWARD)
drivetrain.turn(RIGHT)
numeric posx
numeric posy=0
numeric direction=0
def get_controller_1():
    ax1=controller_1.axis1.position()
    ax2=controller_1.axis2.position()
    drivetrain.set_drive_velocity(ax1, PERCENT)
    drivetrain.set_turn_velocity(ax2*0.50, PERCENT)
    if controller_1.buttonA.pressing():
        motor_3.spin_to_position(90, DEGREES)
    if controller_1.buttonB.pressing():
        motor_3.spin_to_position(0, DEGREES)
    if controller_1.buttonX.pressing():
        motor_4.spin_to_position(90, DEGREES)
    if controller_1.buttonY.pressing():
        motor_4.spin_to_position(0, DEGREES)
    if drivetrain.is_moving():
        direction+=ax2
        posx+=ax1*math.cos(ax2)
        posy+=ax1*math.sin(ax2)
        controller_1.screen.clear_screen()
        controller_1.screen.print("x:",posx,"y:",posy)
while True:
    get_controller_1()
