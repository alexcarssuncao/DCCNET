

import socket


class Transmitter(object):

    def __init__(self, server_name: str, port: int) -> None:

        self.name = server_name
        self.port = port
        self.sock = None
        self.sockaddr = None
        self.running = False



    def transmitter_socket(self) -> None:
        
        '''Creates a UDP socket and returns it
        '''
        
        # =============================================================================
        #                                   DNS LOOKUP
        # ============================================================================= 

        addr_info = socket.getaddrinfo(self.name, self.port, socket.AF_UNSPEC, socket.SOCK_DGRAM)

        for info in addr_info:
            addr_type, _, _, _, sockaddr = info
            try:
                # Create a UDP socket
                sock = socket.socket(addr_type, socket.SOCK_DGRAM)
                sock.settimeout(5)

                # Bind the socket to the address and port
                sock.bind(sockaddr)

                # Just for debugging purposes
                print(f"Server listening on {sockaddr}")

                # ============================================= #
                #      assigns sockets to transmitter object    # 
                # ============================================= #
                self.sock = sock
                self.sockaddr = sockaddr
                return

            except Exception as e:
                print("Failed to bind to", sockaddr, ":", e)
                continue


    def stop(self):

        self.sock.close()
        self.running = False

        print('Transmitter successfully shut down.')





