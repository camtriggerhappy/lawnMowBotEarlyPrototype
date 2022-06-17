from enum import Enum

import RPi.GPIO as GPIO
import time
    
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
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN)
        
        
        
    def updateEncoder(self):

        self.count += self.expectedMotorVelocitySign.value # increment the counter based on whether it should be positive or negative based on the expected motor velocity
        print("called Back")
        
    def setVelocitySign(self, expectedSign:expectedMotorVelocitySign ):
        self.expectedSign = expectedSign

    def update(self):
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback = self.updateEncoder, bouncetime = 20)

        
    

if __name__ == "__main__":
    sensor = encoder(3 , "right")
    sensor.setVelocitySign(expectedMotorVelocitySign.forward)
    sensor.update()
    while True:

        print(sensor.count)
        time.sleep(.1)

        
    
    
