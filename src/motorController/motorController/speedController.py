
import lgpio

def main():
    handler = lgpio.gpiochip_open(0)
    diff = differentialDrive(handler)
    while True:
        diff.forward()
        
    lgpio.gpiochip_close(0)
        

class differentialDrive():
    def __init__(self, h):
        self.h = h
        self.rightMotorSpeed = 15
        self.rightMotorDirectiom = 14
        
        self.leftMotorSpeed = 23
        self.leftMotorDirection = 24
        
        
        
        
    def forward(self):
        lgpio.tx_pwm(self.h, self.rightMotorSpeed,120, 20)
        lgpio.gpio_write(self.h, self.rightMotorDirectiom,1)
        
        lgpio.tx_pwm(self.h, self.leftMotorSpeed,120,  20)
        lgpio.gpio_write(self.h, self.leftMotorDirection, 1)


if __name__ == '__main__':
    main()
