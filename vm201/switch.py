#!/usr/bin/env python3
import os, sys
import time
from VM201RelayCard import *


#------------------------------------------------------------------------------
def main():
    print("----------------------------------------------------------------")
    print("Switch.py script")
    print("----------------------------------------------------------------")
    
    
    sw = VM201RelayCard('10.62.33.22', 9760, None, None, True)
    sw.connect()
    time.sleep(1)
    sw.status()
    
    sw.on_off_toggle('CMD_ON', 6)
    #sw.on_off_toggle('CMD_ON', [6,7,8])
    #sw.on_off_toggle('CMD_ON', 7)
    #sw.on_off_toggle('CMD_ON', 8)
    time.sleep(5)
    sw.on_off_toggle('CMD_OFF', [6,7,8])
    #sw.on_off_toggle('CMD_OFF', 7)
    #sw.on_off_toggle('CMD_OFF', 8)
    
    sw.disconnect()
#------------------------------------------------------------------------------
if __name__ == "__main__":
    exit(main())