import wpilib
import phoenix5
from constants import CanIds


#cd src
#py -3 -m robotpy sim 

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        # Crancons drive
        # Falcons Swerve
        
        self.frontLeftDrive = phoenix5.WPI_TalonSRX(CanIds.frontLeftDrive)
        self.rearLeftDrive = phoenix5.WPI_TalonSRX(CanIds.rearLeftDrive)
        self.frontRightDrive = phoenix5.WPI_TalonSRX(CanIds.frontRightDrive)
        self.rearRightDrive = phoenix5.WPI_TalonSRX(CanIds.rearRightDrive)

        self.frontLeftSteer = phoenix5.WPI_TalonSRX(CanIds.frontLeftSteer)
        self.rearLeftSteer = phoenix5.WPI_TalonSRX(CanIds.rearLeftSteer)
        self.frontRightSteer = phoenix5.WPI_TalonSRX(CanIds.frontRightSteer)
        self.rearRightSteer = phoenix5.WPI_TalonSRX(CanIds.rearRightSteer)

        self.controller = wpilib.XboxController(CanIds.controllerID)

    def teleopInit(self):
        print("teleop initated")

    def teleopPeriodic(self):
        x = self.controller.getLeftX()
        y = self.controller.getLeftY()
        z = self.controller.getRightY()

        print(f"X: {x}, Y: {y}, Z: {z}")


