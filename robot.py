#!/usr/bin/env python3
"""
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    tank drive.
"""

import wpilib
import ctre
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID
from subsystems.drivetrain import Drivetrain 
from subsystems.grabber import Grabber

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """Robot initialization function"""
        LEFT = 1
        RIGHT = 2
        CENTER1 = 3
        CENTER2 = 4
        #GRABBER = 5
        # object that handles basic drive operations
        self.leftTalon = ctre.WPI_TalonSRX(LEFT)
        self.rightTalon = ctre.WPI_TalonSRX(RIGHT)
        self.centerTalon1 = ctre.WPI_TalonSRX(CENTER1)
        self.centerTalon2 = ctre.WPI_TalonSRX(CENTER2)

        #self.grabber = Grabber(ctre.WPI_TalonSRX(GRABBER))

        self.left = wpilib.SpeedControllerGroup(self.leftTalon)
        self.right = wpilib.SpeedControllerGroup(self.rightTalon)

        self.center1 = wpilib.SpeedControllerGroup(self.centerTalon1)
        self.center2 = wpilib.SpeedControllerGroup(self.centerTalon2)

        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)

        # joysticks 1 & 2 on the driver station
        # self.leftStick = wpilib.Joystick(0)
        # self.rightStick = wpilib.Joystick(1)

        self.DEADZONE = 0.4

        self.LEFT = GenericHID.Hand.kLeft
        self.RIGHT = GenericHID.Hand.kRight

        self.driver = wpilib.XboxController(0)

    def autonomousInit(self):
        self.myRobot.tankDrive(0.8, 0.8)

    def autonomousPeriodic(self):
        self.myRobot.tankDrive(1, 0.5)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def setCenters(self, speed_value):
        self.center1.set(speed_value)
        self.center2.set(-speed_value)

    def deadzone(self, val, deadzone):
        if abs(val) < deadzone:
            return 0
        return val

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""

        # right = self.driver.getY(self.RIGHT)
        # left = self.driver.getY(self.LEFT)

        # self.myRobot.tankDrive(right, left)
        # center_speed = self.driver.getX(self.RIGHT)

        DEADZONE = 0.2
        MAX_ACCELERATION = 0.3
        goal_forward = -self.driver.getY(RIGHT)
        rotate = self.driver.getX(LEFT)

        MAX_FORWARD = 1.0
        MAX_ROTATE = 1.0

        goal_forward = deadzone(goal_forward * MAX_FORWARD, DEADZONE)
        rotate = deadzone(rotate * MAX_ROTATE, DEADZONE)

        delta = goal_forward - self.forward

        if abs(delta) < MAX_ACCELERATION:
            self.forward += delta
        else:
            self.forward += MAX_ACCELERATION * sign(delta)

        if self.driver.getXButton():
            self.drivetrain.stop()
        else:
            self.drivetrain.arcade_drive(self.forward, rotate)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        #self.setCenters(self.deadzone(center_speed, self.DEADZONE))

        left_trigger = self.driver.getTriggerAxis(LEFT)
        right_trigger = self.driver.getTriggerAxis(RIGHT)

        TRIGGER_LEVEL = 0.4

        if abs(left_trigger) > TRIGGER_LEVEL:
            self.setCenters(1.0)
        elif abs(right_trigger) > TRIGGER_LEVEL:
            self.setCenters(-1.0)
        
    def deadzone(val, deadzone):
        if abs(val) < deadzone:
            return 0
        return val    


if __name__ == "__main__":
    wpilib.run(MyRobot)
