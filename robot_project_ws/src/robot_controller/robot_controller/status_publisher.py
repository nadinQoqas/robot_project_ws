import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusPublisher(Node):
    def __init__(self):
        super().__init__('status_publisher')
        self.publisher_=self.create_publisher(String, 'robot/status', 10)
        self.timer =self.create_timer(2.0.self.publish_status)
        self.count =0
        self.get_logger().info('Status Publisher Node started!')
    
    def publish_status(self):
        msg=String()
        msg.data=f'Robot is running... ({self.count})'
        self.publisher_.publisher(msg)
        self.get_logger().info(f'Published:{msg.data}')
        self.count+=1

def main(args=None):
    rclpy.init(args=args)
    node=StatusPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node,destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
