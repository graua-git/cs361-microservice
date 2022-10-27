import rpyc
import math


# Square root microservice
class SquareRootService(rpyc.Service):

    def on_connect(self, conn):
        print("Connection started...")

    def on_disconnect(self, conn):
        print("Connection ended.")

    """
    Retrieve the square root of num
    to call: run connection.root.squareroot(num)
    """
    def exposed_squareroot(self, num):
        return math.sqrt(num)


if __name__ == '__main__':
    # Start server
    port_num = 18861
    print(f"Starting SquareRootService on port: {port_num}...")
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(SquareRootService, port=port_num)
    t.start()
