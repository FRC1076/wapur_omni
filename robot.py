#!/usr/bin/env python3
"""
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    tank drive.
"""

import wpilib
from wpilib.drive import DifferentialDrive

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


        self.center = wpilib.SpeedControllerGroup(self.centerTalon1, self.centerTalon2)

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
