

def checksum(frame: bytes) -> bytes:
    

    # a) setting the reserved bytes for the checksum to zero
    for i in range(8, 10):
        frame[i] = 0
    
    # b) converting the data frame into a list of 16-bit words:
    words = [frame[i] + (frame[i + 1] << 8) for i in range(0, len(frame), 2)]
    
    # c) calculating the 32-bit sum
    checksum = sum(words)
    
    # d) folding 32-bit sum into 16 bits
    while checksum >> 16:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)
    
    # e) taking one's complement
    checksum = ~checksum & 0xFFFF
    
    # f) return the checksum
    return checksum


