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
        lgpio.gpio_write(self.h, self.leftMotor,1)
        lgpio.gpio_write(self.h, self.rightMotor,1)


if __name__ == '__main__':
    main()
