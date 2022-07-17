
import lgpio
from rclpy.node import Node
import rclpy
from std_msgs import String


def main():
    rclpy.init()
    driveTrain = differentialDrive()
    rclpy.spin(driveTrain)
    
 

class differentialDrive(Node):
    def __init__(self, h):
        self.h = h
        self.rightMotorSpeed = 14
        self.rightMotorDirectiom = 15
        
        self.leftMotorSpeed = 24
        self.leftMotorDirection = 23
        
        self.Direction = "forward"
        self.publishDir = self.create_publisher(String, "direction", 12)
        
        
    def publishDir(self):
        msg = String()
        
        self.publishDir.publish(msg)
        
        
        
        
    def forward(self):
        lgpio.tx_pwm(self.h, self.rightMotorSpeed,120,pwm_duty_cycle=20)
        lgpio.gpio_write(self.h, self.rightMotorDirectiom,0)
        
        lgpio.tx_pwm(self.h, self.leftMotorSpeed,120, pwm_duty_cycle=20)
        lgpio.gpio_write(self.h, self.leftMotorDirection, 0)
        print("moving")


if __name__ == '__main__':
    main()
