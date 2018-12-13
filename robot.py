#!/usr/bin/env python3
"""
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    tank drive.
"""

import wpilib
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import SpeedController

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """Robot initialization function"""
        LEFT = 0
        RIGHT = 1
        CENTER = 2
        # object that handles basic drive operations
        self.left = wpilib.Talon(LEFT)
        self.right = wpilib.Talon(RIGHT)
        self.center = wpilib.Talon(CENTER)

        self.left = wpilib.SpeedController(self.left)
        self.right = wpilib.SpeedController(self.right)
	    self.center = SpeedController(self.center)
        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)

        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        self.myRobot.tankDrive(self.leftStick.getY() * -1, self.rightStick.getY() * -1)


if __name__ == "__main__":
    wpilib.run(MyRobot)
