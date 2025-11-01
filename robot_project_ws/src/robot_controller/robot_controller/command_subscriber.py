import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandSubscriber(Node):
    def __init__(self):
        super().__init__('command_subscriber')
        self.subscriber_=self.create_subscription(String,'/robot/command',self.callback,10)
        self.subscriber_
        self.get_logger().info('Command Subscriber Node Started!')

    def callback(self,msg):
        command=msg.data.lower()
        if command in ['start', 'stop', 'reset']:
            self.get_logger().warn(f'Recieved valid command:{command}')
        else:
            self.get_logger().warn(f'Unknown command:{command}')
    
def main(args=None):
    rclpy.init(args=args)
    node=CommandSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
