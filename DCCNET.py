
from internet_checksum import checksum
from typing import Union



CONTROL_FLAGS = {
    'ACK': 0x80,
    'END': 0x40,
    'reserved': 0x3f
}

SYNC: int = 0xDCC023C2



class dccnet_frame(object):


    def __init__(self, frame: Union[bytes,None] = None) -> None:
       
        # The frame format:
        # 0        4        8        10        12    14    15
        # +--------+--------+---------+---------+-----+-----+------ ... ---+
        # |  SYNC  |  SYNC  | chksum  | length  | ID  |flags| DATA         |
        # +--------+--------+---------+---------+-----+-----+------ ... ---+

        self.frame: Union[bytes,None] = frame  # N bytes. Complete frame to send or receive
        
        self.sync1: bytes = b''    # 4 bytes at position: 0-3
        self.sync2: bytes = b''    # 4 bytes at position: 4-7
        self.chksum: bytes = b''   # 2 bytes at position: 8-9
        self.length: bytes = b''   # 2 bytes at position: 10-11 
        self.ID: bytes = b''       # 2 bytes at position: 12-13
        self.flag: bytes = b''     # 1 byte at position: 14
        self.data: bytes = b''     # X bytes at position: 15-x
      
     
    # ======================================================================== #
    #                               SETTER METHODS                             #
    # ________________________________________________________________________ #
    
    '''Every set_*** method can receive an argument or not. If it does, it will assign that
       value to the appropriate variable. If it does not receive an argument, it will assume
       the variable's value is in its frame.
    '''   
    
    def set_sync1(self, *args) -> None:
        
        if args:
            self.sync1 = args[0]
        elif self.frame is not None:
            self.sync1 = self.frame[0:4]
    #---
    def set_sync2(self, *args) -> None:
        
        if args:
            self.sync2 = args[0]
        elif self.frame is not None:
            self.sync2 = self.frame[4:8]
    #---   
    def set_chksum(self, *args) -> None:
        
        if args:
            self.chksum = args[0]
        elif self.frame is not None:
            self.chksum = self.frame[8:10]
    #---                      
    def set_length(self, *args) -> None:
    
        if args:
            self.length = args[0]
        elif self.frame is not None:
            self.length = self.frame[10:12]
    #---
    def set_ID(self, *args) -> None:
        
        if args:
            self.ID = args[0]
        elif self.frame is not None:    
            self.ID = self.frame[12:14]
    #---
    def set_flag(self, *args) -> None:
        
        if args:
            self.flag = args[0]
        elif self.frame is not None:        
            self.flag = self.frame[14:15]
    #---
    def set_data(self, *args) -> None:
        
        if args:
            self.data = args[0]
        elif self.frame is not None:
            self.data = self.frame[15:]
       
    # ======================================================================== #
    #                               GETTER METHODS                             #
    # ________________________________________________________________________ #
        
    def get_sync1(self) -> bytes:
        
        return self.sync1
    #---
    def get_sync1(self) -> bytes:
        
        return self.sync1
    #---
    def get_chksum(self) -> bytes:
        
        return self.chksum
    #---
    def get_length(self) -> bytes:
        
        return self.length
    #---
    def get_ID(self) -> bytes:
        
        return self.ID
    #---
    def get_flag(self) -> bytes:
    
        return self.flag
    #---
    def get_data(self) -> bytes:
        
        return self.data
    
    # ======================================================================== #
    #                        DCCNET PROTOCOL METHODS                           #
    # ________________________________________________________________________ #
     def parse_frame(self):
        
        self.set_sync1()
        self.set_sync2()
        self.set_chksum()
        self.set_length()
        self.set_ID()
        self.set_flag()
        self.set_data()


    def calculate_checksum(self) -> bytes:
        
        '''Runs the internet checksum algorithm on the trasnmission frame's entire body
           Returns: the checksum in bytes
        '''
        self.chksum = checksum(self.frame)
        return self.chksum
    

    def create_ack_frame(self, previous_ID):
        
        ack_frame =  dccnet_frame(None)
        
        ack_frame.set_sync1(0xDCC023C2)
        ack_frame.set_sync2(0xDCC023C2)
        ack_frame.set_length(0)
        ack_frame.set_ID(~previous_ID)
        ack_frame.set_flag(CONTROL_FLAGS['ACK'])
        ack_frame.set_data(None)
        
        return ack_frame
        
        
    def display_frame(self):
        
        print(f"SYNC1: {self.sync1.hex()}")
        print(f"SYNC2: {self.sync2.hex()}")
        print(f"Checksum: {self.chksum.hex()}")
        print(f"Length: {self.length.hex()}")
        print(f"ID: {self.ID.hex()}")
        print(f"Flag: {self.flag.hex()}")
        print(f"Data: {self.data.hex()}")
            