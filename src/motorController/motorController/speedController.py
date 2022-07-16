
import lgpio
from pyEncoder.pyEncoder.encoderReader import encoder


def main():
    handler = lgpio.gpiochip_open(0)
    diff = differentialDrive(handler)
    while True:
        diff.forward()
        
    lgpio.gpiochip_close(0)
        

class differentialDrive():
    def __init__(self, h):
        self.h = h
        self.rightMotorSpeed = 14
        self.rightMotorDirectiom = 15
        
        self.leftMotorSpeed = 24
        self.leftMotorDirection = 23
        
        
        
        
    def forward(self):
        lgpio.tx_pwm(self.h, self.rightMotorSpeed,120,pwm_duty_cycle=20)
        lgpio.gpio_write(self.h, self.rightMotorDirectiom,1)
        
        lgpio.tx_pwm(self.h, self.leftMotorSpeed,120, pwm_duty_cycle=20)
        lgpio.gpio_write(self.h, self.leftMotorDirection, 1)
        print("moving")


if __name__ == '__main__':
    main()
