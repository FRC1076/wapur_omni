import wpilib
import ctre
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID

class Drivetrain:
    """
    The drivetrain class handles driving around as well as shifting between
    low and high gear
    """

    def __init__(self, left, right):
        
        self.robot_drive = wpilib.drive.DifferentialDrive(left, right)

        self.right = right
        self.left = left

    def arcade_drive(self, forward, rotate):
        self.robot_drive.arcadeDrive(forward, rotate)

    def stop(self):
        self.robot_drive.stopMotor()
