
import sys
from typing import Tuple, List, Union, Dict

from transmitter import *
from receiver import *


def Parse_Cmd_Args(arguments: list[str]) -> Tuple[str, int, str, str, str]:
    
    try:
        application = arguments[1]
        
        if(application == '-s'):
            
            port = arguments[2]
            IP = ''
            
        if(application == '-c'):
            
            port, IP = arguments[2].split(':')

        in_file = arguments[3]
        out_file = arguments[4]
        
    except IndexError:
        print('Usage: >python ./dccnet-xfer <app> <PORT:IP> <INPUT> <OUTPUT>')
        exit(0)
    return application, port, IP, in_file, out_file





def main() -> None:
    
    app, port, IP, in_f, out_f = Parse_Cmd_Args(sys.argv)

    print(f'App = {app}, port = {port}, IP = {IP}, in_f = {in_f}, out_f = {out_f}')





if __name__ == '__main__':
    
    main()
