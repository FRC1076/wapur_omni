import ctre
import wpilib
from wpilib import DoubleSolenoid
from wpilib.interfaces import GenericHID

import autonomous
from subsystems.drivetrain import Drivetrain 

LEFT = GenericHID.Hand.kLeft
RIGHT = GenericHID.Hand.kRight

#Motor IDs

LEFT1_ID = 0
LEFT2_ID = 0
RIGHT1_ID = 0
RIGHT2_ID = 0
CENTER_ID = 0

Class Robot(wpilib.IterativeRobot):
    def robotInit(self):
	left1 = ctre.WPI_TalonSRX(LEFT1_ID)
	left2 = ctre.WPI_TalonSRX(LEFT2_ID)
	left = wpilib.SpeedControllerGroup(left1, left2)
	left1.setNeutralMode(ctre.NeutralMode.Brake)
	left2.setneutralMode(ctre.NeutralMode.Brake)

	right1 = ctre.WPI_TalonSRX(RIGHT1_ID)
        right2 = ctre.WPI_TalonSRX(RIGHT2_ID)
        right = wpilib.SpeedControllerGroup(right1, right2)
        right1.setNeutralMode(ctre.NeutralMode.Brake)
        right2.setNeutralMode(ctre.NeutralMode.Brake)

	center = ctre.WPI.TalonSRX(CENTER_ID)
	#speedcontrollergroup??

	self.drivetrain = Drivetrain(left, right, center)
	
	self.driver = wpilib.XboxController(0)
	self.operator = wpilib.XboxController(1)

	self.auto_exec = iter([])

	def robotPeriodic(self):
	
	def teleopInit(self):

	def teleopPeriodic(self):
	    forward = self.driver.getY(RIGHT)
	    rotate = self.driver.getX(LEFT)

		
