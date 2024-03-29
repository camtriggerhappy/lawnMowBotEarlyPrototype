from datetime import datetime
from enum import Enum
import math

import pigpio

import time
    
class expectedMotorVelocitySign(Enum):
    forward = 1
    reverse = -1
    
    
    

class encoder():
    
    def __init__(self, pin:int, side:str, distPerTick:float, tickPerRot):
        """

        Args:
            pin (int): the pin number the encoder is on
            side (str): what position is the encoder located in
        """
        
        #super().__init__(side + "_side_node")
    
        self.pin = pin
        self.side = side
        self.count = 0 # the internal encoder count
        self.prevTime = datetime.now()
        self.distPerTick = distPerTick
        self.tickPerRot = tickPerRot
        self.radius = 32.5 / 1000
        self.velocity = 0
        self.h = pigpio.pi()
    

        self.h.callback(self.pin, pigpio.EITHER_EDGE, self.updateEncoder)

        
        
        
        
    def updateEncoder(self, channel):
        timeDiff = datetime.now() - self.prevTime
        self.count += self.expectedSign.value # increment the counter based on whether it should be positive or negative based on the expected motor velocity
        print("called Back")
        self.prevTime = datetime.now()
        self.velocity = self.expectedSign.value * ((math.pi/10)/timeDiff.total_seconds()) * self.radius
        
    def setVelocitySign(self, expectedSign:expectedMotorVelocitySign ):
        self.expectedSign = expectedSign
        
    def getDistance(self):
        return self.radius * (self.count / self.tickPerRot)
    
    def getVelocity(self):
        return self.velocity * self.radius



        
    

if __name__ == "__main__":
    sensor = encoder(38 , "right", ((math.pi/10) * (32.5/1000)), 20)
    sensor.setVelocitySign(expectedMotorVelocitySign.forward)

    while True:

        print(sensor.count)
        print(f"{sensor.getVelocity()} m/s")
        time.sleep(.1)

        
    
    
