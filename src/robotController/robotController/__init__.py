
import math
from rclpy.node import Node
import rclpy
import tf2_geometry_msgs
import geometry_msgs
import nav_msgs
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from tf2_ros import transform_broadcaster, TransformStamped, TransformBroadcaster

    


class Quaternion:
    w: float
    x: float
    y: float
    z: float


    
    
    

class driveController(Node):
    def __init__(self):
        super().__init__("robotController")
        self.leftEncoder = encoder(3, "left", 5,20)
        self.rightEncoder = encoder(3, "right", 5,20)
        self.wheelBase = .104
        self.odomBrodcaster = TransformBroadcaster(self)
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.pitch = 0
        self.yaw = 0
        self.roll = 0
        self.previousCallTime = self.get_clock().now()
        self.odom = Odometry()
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.updatePose)
        
        
        self.publishOdom = self.create_publisher(
            Odometry,
            "odom",
            20,
        )
        
        self. commandSubscription = self.create_subscription(
            Twist,
            "cmd_vel",
            self.setSpeedGoals,
            12
            )
        
        
        
    def getVelocity(self):
        return self.rightEncoder.getVelocity() + self.leftEncoder.getVelocity()
    
    def getAngularVelocity(self):
        return (self.rightEncoder.getVelocity() + self.leftEncoder.getVelocity())/self.wheelBase
    
    def quaternion_from_euler(self):

        cy = math.cos(self.rotation * 0.5)
        sy = math.sin(self.rotation * 0.5)
        cp = math.cos(self.pitch * 0.5)
        sp = math.sin(self.pitch * 0.5)
        cr = math.cos(self.roll * 0.5)
        sr = math.sin(self.roll * 0.5)

        q = Quaternion()
        q.w = cy * cp * cr + sy * sp * sr
        q.x = cy * cp * sr - sy * sp * cr
        q.y = sy * cp * sr + cy * sp * cr
        q.z = sy * cp * cr - cy * sp * sr
        return q 

    def updatePose(self):
        currentTime = self.get_clock().now()
        
        self.odomTrans:TransformStamped = TransformStamped()
        self.odomTrans.header.stamp = self.get_clock().now().to_msg()
          
        self.odomTrans.header.frame_id = "odom"
        self.odomTrans.child_frame_id = "base_link"
   
        self.odomTrans.transform.translation.x = float(self.x)
        self.odomTrans.transform.translation.y = float(self.y)
        self.odomTrans.transform.translation.z = 0.0
        print("quaternion")

        Quaternion = self.quaternion_from_euler()
        self.odomTrans.transform.rotation.w = Quaternion.w 
        self.odomTrans.transform.rotation.x = Quaternion.x
        self.odomTrans.transform.rotation.y = Quaternion.y
        self.odomTrans.transform.rotation.z = Quaternion.z
        
        
        
        self.odomBrodcaster.sendTransform(self.odomTrans)
        
        
        self.rotation += self.getAngularVelocity() * (currentTime - self.previousCallTime).nanoseconds/1e9
        self.x
        self.y
        self.odom:Odometry
        self.odom._header.stamp = self.get_clock().now().to_msg()
        self.odom.header.frame_id =  "odom"
        self.odom.pose.pose.position.x = float(self.x)
        self.odom.pose.pose.position.y = float(self.y) 
        self.odom.pose.pose.orientation.w = Quaternion.w 
        self.odom.pose.pose.orientatio.n.x = Quaternion.x 
        self.odom.pose.pose.orientation.y = Quaternion.y 
        self.odom.pose.pose.orientation.z = Quaternion.z
        
    
        
        self.odom.child_frame_id = "base_link"
        self.odom.twist.twist.linear.x = self.getVelocity()
        self.odom.twist.twist.linear.y = self.getVelocity()
        self.odom.twist.twist.angular.z = self.getAngularVelocity()
        
        self.publishOdom.publish(self.odom)
        print("published odom")
        
        self.lastTime = currentTime
        
     
    
    def setSpeedGoals(self):
        pass


    
    
    
    
from datetime import datetime
from enum import Enum
import math

import pigpio

import time
    
class expectedMotorVelocitySign(Enum):
    forward = 1
    reverse = -1
    
    
    

class encoder():
    
    def __init__(self, pin:int, side:str, distPerTick:float, tickPerRot):
        """

        Args:
            pin (int): the pin number the encoder is on
            side (str): what position is the encoder located in
        """
        
        #super().__init__(side + "_side_node")
    
        self.pin = pin
        self.side = side
        self.count = 0 # the internal encoder count
        self.prevTime = datetime.now()
        self.distPerTick = distPerTick
        self.tickPerRot = tickPerRot
        self.radius = 32.5 / 1000
        self.velocity = 0
        self.h = pigpio.pi()
    

        self.h.callback(self.pin, pigpio.EITHER_EDGE, self.updateEncoder)

        
        
        
        
    def updateEncoder(self, channel):
        timeDiff = datetime.now() - self.prevTime
        self.count += self.expectedSign.value # increment the counter based on whether it should be positive or negative based on the expected motor velocity
        print("called Back")
        self.prevTime = datetime.now()
        self.velocity = self.expectedSign.value * ((math.pi/10)/timeDiff.total_seconds()) * self.radius
        
    def setVelocitySign(self, expectedSign:expectedMotorVelocitySign ):
        self.expectedSign = expectedSign
        
    def getDistance(self):
        return self.radius * (self.count / self.tickPerRot)
    
    def getVelocity(self):
        return self.velocity * self.radius



    
def main():
    rclpy.init()
    controller = driveController()
    #sensor = encoder(38 , "right", ((math.pi/10) * (32.5/1000)), 20)
    #sensor.setVelocitySign(expectedMotorVelocitySign.forward)
    
    print("running")

    rclpy.spin(controller)
    
    



            
    
    
if __name__ == "main":
    main()
    
