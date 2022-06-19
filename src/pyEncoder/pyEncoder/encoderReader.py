from enum import Enum
import rclpy
from rclpy.node import Node

import RPi.GPIO as GPIO
import time
from 
    
class expectedMotorVelocitySign(Enum):
    forward = 1
    reverse = -1
    
    
    

class encoder(Node):
    
    def __init__(self, pin:int, side:str):
        """

        Args:
            pin (int): the pin number the encoder is on
            side (str): what position is the encoder located in
        """
        
        super().__init__(side + "_side_node")
    
        self.pin = pin
        self.side = side
        self.count = 0 # the internal encoder count
    
        self.sideSubscriber = self.create_subscription(
            
            
        )
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN)
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback = self.updateEncoder, bouncetime = 20)
        
        
        
    def updateEncoder(self, channel):

        self.count += self.expectedSign.value # increment the counter based on whether it should be positive or negative based on the expected motor velocity
        print("called Back")
        
    def setVelocitySign(self, expectedSign:expectedMotorVelocitySign ):
        self.expectedSign = expectedSign



        
    

if __name__ == "__main__":
    sensor = encoder(3 , "right")
    sensor.setVelocitySign(expectedMotorVelocitySign.forward)

    while True:

        print(sensor.count)
        time.sleep(.1)

        
    
    
