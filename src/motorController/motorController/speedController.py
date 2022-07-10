import lgpio

def main():
    diff = differentialDrive()
    while True:
        diff.forward()

class differentialDrive():
    def __init__(self):
        self.h = lgpio.gpiochip_open(0)
        self.rightMotorSpeed = 15
        self.rightMotorDirectiom = 14
        
        
    def forward(self):
        lgpio.gpio_write(self.h, self.rightMotorSpeed,0)
        lgpio.gpio_write(self.h, self.rightMotorDirectiom,1)


if __name__ == '__main__':
    main()
