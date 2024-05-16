# DCCNET
emulating data link layer with DCCNET protocol

modules:

transmitter.py -- implements the server functions
receiver.py -- implements the client functions
DCCNET.py -- implements the functions related to the protocol (building, checking, and parsing frames)
internet_checksum.py -- implements the MD5 checksum algorithm
dccnet-xfer.py -- currently, it only parses the command line arguments. To test code use tp2_debug.py

tp2_debug.py -- file to test my code. Currently, it launches the server and client, and establishes a connection.
