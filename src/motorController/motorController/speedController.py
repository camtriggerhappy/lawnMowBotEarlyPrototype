

import lgpio
from rclpy.node import Node
import rclpy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def main():
    rclpy.init()
    driveTrain = differentialDrive()
    print("started")
    rclpy.spin(driveTrain)
    
 

class differentialDrive(Node):
    def __init__(self):
        super().__init__("differentialDrive")
        self.h = lgpio.gpiochip_open(0)
        self.rightMotorSpeed = 14
        self.rightMotorDirectiom = 15
        
        self.leftMotorSpeed = 24
        self.leftMotorDirection = 23
        
        self.Direction = "forward"
        self.publishDir = self.create_publisher(String, "direction", 12)
        print("creating subscriber")    
        self.twistSubscription = self.create_subscription
        (
    
            Twist,
            "cmd_vel",
            self.setTwist,
            12
        )
        print("created subscriber")    
        
        
        
        
        
        
    def publishDir(self):
        msg = String()
        
        self.publishDir.publish(msg)
        
    def setTwist(self, Twist):
        print("recived")
        self.Twist = Twist
        
        
        
        
        
    def forward(self, speed:float):
        lgpio.tx_pwm(self.h, self.rightMotorSpeed,120,pwm_duty_cycle=speed)
        lgpio.gpio_write(self.h, self.rightMotorDirectiom,0)
        
        lgpio.tx_pwm(self.h, self.leftMotorSpeed,120, pwm_duty_cycle=speed)
        lgpio.gpio_write(self.h, self.leftMotorDirection, 0)
        print("moving")


if __name__ == '__main__':
    main()
