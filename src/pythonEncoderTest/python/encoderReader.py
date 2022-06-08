from enum import Enum
from turtle import forward
    
class expectedMotorVelocitySign(Enum):
    forward = 1
    reverse = -1
    
    
    

class encoder():
    
    def __init__(self, pin:int, side:str):
        """

        Args:
            pin (int): the pin number the encoder is on
            side (str): what position is the encoder located in
        """
        self.pin = pin
        self.side = side
        self.count = 0 # the internal encoder count
        
    def updateEncoder(self, expectedSign:expectedMotorVelocitySign):
        self.expectedSign = expectedSign
        self.count += expectedMotorVelocitySign # increment the counter based on whether it should be positive or negative based on the expected motor velocity
        
        

        
    
    
