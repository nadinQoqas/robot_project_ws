import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelocityPublisher(Node):
    def __init__(self):
        super().__init('Velocity_publisher')
        self.publisher=self.create_publisher(Twist,'/rcmd_vel',10)
        self.timer=self.create_timer(1.0,self.publish_velocity)
        self.step=0
        self.get_logger().info('Velocity publisher Node Started!')

    def publish_velocity(self):
        msg=Twist()
        if self.step % 2 ==0:
            msg.linear.x=0.2
            msg.angular.z=0.0
        else:
            msg.linear.x=0.0
            msg.angular.z=0.5
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published velocity: linear.x={msg.linear.x},angular.z={msg.angular.z}')
        self.step+=1
    
def main(args=None):
    rclpy.init(args=args)
    node=VelocityPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
