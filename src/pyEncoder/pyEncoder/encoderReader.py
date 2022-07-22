from datetime import datetime
from enum import Enum
import math
import rclpy
from rclpy.node import Node

import RPi.GPIO as GPIO
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
    

        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN)
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback = self.updateEncoder, bouncetime = 20)
        
        
        
    def updateEncoder(self, channel):
        timeDiff = datetime.now() - self.prevTime
        self.count += self.expectedSign.value # increment the counter based on whether it should be positive or negative based on the expected motor velocity
        print("called Back")
        self.prevTime = datetime.now()
        self.velocity = self.expectedSign.value * ((math.pi/10)/timeDiff) * self.radius
        
    def setVelocitySign(self, expectedSign:expectedMotorVelocitySign ):
        self.expectedSign = expectedSign
        
    def getDistance(self):
        return self.radius * (self.count / self.tickPerRot)
    
    def getVelocity(self):
        return self.velocity * self.radius



        
    

if __name__ == "__main__":
    sensor = encoder(20 , "right", ((math.pi/10) * (32.5/1000)), 20)
    sensor.setVelocitySign(expectedMotorVelocitySign.forward)

    while True:

        print(sensor.count)
        print(sensor.getVelocity + "m/s")
        time.sleep(.1)

        
    
    
