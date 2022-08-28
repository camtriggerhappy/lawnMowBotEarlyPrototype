

import pigpio 
from rclpy.node import Node
import rclpy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from simple_pid import PID


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
        
        self.Twist = Twist
        self.pid = PID(1, 0, .3, output_limits=(-126, 126))
        
        self.Direction = "forward"
        print("creating subscriber")    
        self.twistSubscription = self.create_subscription(
    
            Twist,
            "cmd_vel",
            self.setTwist,
            12
        )
        print("created subscriber")    
        
    def setTwist(self, Twist):
        print("recived")
        self.Twist = Twist
        
        
        
        
        
    def drive(self, speed:float):
        self.pid.setpoint = speed
        output = self.pid(speed)
        sign = 0
        if self.Twist.linear.x > 0:
            sign = 1
        elif self.Twist.linear.x < 0:
            sign = 0
        direction = sign
    
        self.Twist
        self.h.set_PWM_dutycycle(self.leftMotorSpeed,speed)
        self.h.write(self.rightMotorDirectiom,direction)
        
        self.h.set_PWM_dutycycle(self.rightMotorDirectiom,speed)
        self.h.write(self.leftMotorDirection, direction)
        print("moving")


if __name__ == '__main__':
    main()
