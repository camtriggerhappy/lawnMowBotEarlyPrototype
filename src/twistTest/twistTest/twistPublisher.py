from rclpy.node import Node
import rclpy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def main():
    rclpy.init()
    driveTrain = testTwist()
    print("started")
    rclpy.spin(driveTrain)
    
 

class testTwist(Node):
    def __init__(self):
        super().__init__("testTwist")
 
        print("creating publisher")    
        self.twistSubscription = self.create_publisher
        (
    
            Twist,
            "cmd_vel",
            12
        )
        print("created subscriber")    
        
        
        
        
        
        
    def publishTwist(self):
        msg = Twist()
        msg.linear.x = 1
        
        
        self.publishDir.publish(msg)
        
    def setTwist(self, Twist):
        print("recived")
        self.Twist = Twist
        
        
        
        
        
    def forward(self, speed:float):

        print("moving")


if __name__ == '__main__':
    main()
