
from encoderReader import encoder
from rclpy.node import Node
import rclpy
import common_interfaces
import tf2_geometry_msgs
import geometry_msgs
import nav_msgs
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from tf2_ros import transform_broadcaster, TransformStamped
import tf_transformations


class driveController(Node):
    def __init__(self):
        self.leftEncoder = encoder(3, "left", 5)
        self.rightEncoder = encoder(3, "right", 5)
        self.wheelBase = .104
        self.odomBrodcaster = transform_broadcaster()
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.previousCallTime = self.get_clock().now()
        
        self. commandSubscription = self.create_subscription(
            geometry_msgs.Twist,
            "cmd_vel",
            self.setSpeedGoals,
            12
            )
        
        self.publishOdom = self.create_publisher(
            Odometry,
            "odom",
            self.updatePose,
        )
        
        
        
    def getVelocity(self):
        return self.rightEncoder.getVelocity() + self.leftEncoder.getVelocity()
    
    def getAngularVelocity(self):
        return (self.rightEncoder.getVelocity() + self.leftEncoder.getVelocity())/self.wheelBase
    
    def updatePose(self):
        currentTime = self.get_clock().now()
        
        self.odomTrans:TransformStamped
        self.odomTrans.header.stamp = currentTime
          
        self.odomTrans.header.frame_id = "odom"
        self.odomTrans.child_frame_id = "base_link"
   
        self.odomTrans.transform.translation.x = self.x
        self.odomTrans.transform.translation.y = self.y
        self.odomTrans.transform.translation.z = 0.0
        self.odomTrans.transform.rotation = tf_transformations.createQuaternionMsgFromYaw(self.rotation)
        
        self.odomBrodcaster.sendTransform(self.odomTrans)
        
        
        self.angle += self.getAngularVelocity() * (currentTime - self.previousCallTime)
        self.x
        self.y
        self.odom:Odometry
        self.odom._header.stamp = self.get_clock().now()
        self.odom.header.frame_id =  "odom"
        self.odom.pose = Pose(self.x, self.y, self.rotation)
        
        self.odom.child_frame_id = "base_link"
        self.odom.twist.twist.linear.x = self.getVelocity()
        self.odom.twist.twist.linear.y = self.getVelocity()
        self.odom.twist.twist.angular.z = self.getAngularVelocity()
        
        self.publishOdom.publish(self.odom)
        
        self.lastTime = currentTime
        
     
    
    def setSpeedGoals(self):
        pass
    
    
    
    
    
    
    
if __name__ == "main":
    controller = driveController()
    rclpy.spin(controller)