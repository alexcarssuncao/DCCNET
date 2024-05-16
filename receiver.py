

import socket


class Receiver(object):

    def __init__(self, host_name: str, port: int) -> None:

        self.name = host_name
        self.port = port
        self.sock = None
        self.sockaddr = None
        self.running = False



    def receiver_socket(self) -> None:

        # =============================================================================
        #                                   DNS LOOKUP
        # ============================================================================= 
    
        '''
        SOCK_DGRAM := chooses UDP instead of the default TCP
        '''
        addr_info = socket.getaddrinfo(self.name, self.port, socket.AF_UNSPEC, socket.SOCK_DGRAM)

        # Loop to try both IPv4 and IPv6 addresses
        for info in addr_info:
            
            addr_type, _, _, _, sockaddr = info
            
            try:
                sock = socket.socket(addr_type, socket.SOCK_DGRAM)
                sock.settimeout(5)
                sock.connect(sockaddr)
                
                # Just for debugging
                print(f"Client connected to {sockaddr}")

                # ===================================================== #
                #       assigns the socket to the receiver object       # 
                # ===================================================== #
                self.sock = sock
                self.sockaddr = sockaddr
                return

            except Exception as e:
                print("Failed to connect to", sockaddr, ":", e)
                continue
    
        raise Exception("Unable to connect to server")


    def stop(self):

        self.sock.close()
        self.running = False

        print('Receiver successfully shut down.')

    