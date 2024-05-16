


from transmitter import *
from receiver import *
import threading
import time


def start_server():

    server = Transmitter('localhost', 12345)
    server_thread = threading.Thread(target = server.transmitter_socket)
    server_thread.start()
    return server, server_thread

def start_client():

    client = Receiver('localhost',12345)
    client.receiver_socket()
    return client

if __name__ == "__main__":

    # Start server thread
    server, server_thread = start_server()
    
    # Give the server a moment to start
    time.sleep(1)
    
    # Run client in main thread
    client = start_client()

    server.stop()
    client.stop()

    server_thread.join()

