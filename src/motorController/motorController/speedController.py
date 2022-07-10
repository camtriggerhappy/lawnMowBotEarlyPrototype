import lgpio

def main():
    diff = differentialDrive()
    diff.forward()

class differentialDrive():
    def __init__(self):
        self.h = lgpio.gpiochip_open(0)
        self.rightMotor = 12
        self.leftMotor = 33
        
        
    def forward(self):
        lgpio.tx_pwm(self.h, self.leftMotor,80)
        lgpio.tx_pwm(self.h, self.rightMotor,80)


if __name__ == '__main__':
    main()
