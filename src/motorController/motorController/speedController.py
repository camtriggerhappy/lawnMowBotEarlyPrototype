

import pigpio 
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
        self.h = pigpio.pi()
        self.rightMotorSpeed = 14
        self.rightMotorDirectiom = 15
        
        self.leftMotorSpeed = 24
        self.leftMotorDirection = 23
        
        self.Direction = "forward"
        print("creating subscriber")    
        self.twistSubscription = self.create_subscription(
    
            Twist,
            "cmd_vel",
            self.setTwist,
            12
        )
        print("created subscriber")    
        
        self.publishDir = self.create_publisher(String, "direction", 12)
  
        
        
        
        
        
    def publishDir(self):
        msg = String()
        
        self.publishDir.publish(msg)
        
    def setTwist(self, Twist):
        print("recived")
        self.Twist = Twist
        
        
        
        
        
    def forward(self, speed:float):
        self.h.set_PWM_dutycycle(self.leftMotorSpeed,speed)
        self.h.write(self.rightMotorDirectiom,0)
        
        self.h.set_PWM_dutycycle(self.rightMotorDirectiom,speed)
        self.h.write(self.leftMotorDirection, 0)
        print("moving")


if __name__ == '__main__':
    main()
