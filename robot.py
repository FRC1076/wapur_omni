#!/usr/bin/env python3
"""
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    tank drive.
"""

import wpilib
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """Robot initialization function"""
        LEFT = 0
        RIGHT = 1
        CENTER1 = 2
        CENTER2 = 3
        # object that handles basic drive operations
        self.leftTalon = wpilib.Talon(LEFT)
        self.rightTalon = wpilib.Talon(RIGHT)
        self.centerTalon1 = wpilib.Talon(CENTER1)
        self.centerTalon2 = wpilib.Talon(CENTER2)

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
        line = self.driver.getY(self.RIGHT)
        rotate = self.driver.getX(self.LEFT)
        self.myRobot.tankDrive(line, rotate)


if __name__ == "__main__":
    wpilib.run(MyRobot)
