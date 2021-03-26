#!/usr/bin/env python3
import os, sys
import time
from VM201RelayCard import *


#------------------------------------------------------------------------------
def main():
    print("----------------------------------------------------------------")
    print("Switch.py script")
    print("----------------------------------------------------------------")
    
    
    sw = VM201RelayCard('10.62.33.22')
    sw.connect()
    #sw.status()
    
    sw.on_off_toggle('CMD_ON', 7)
    #sw.on_off_toggle('CMD_ON', 7)
    #time.sleep(5)
    #sw.on_off_toggle('CMD_OFF', 7)
    
#------------------------------------------------------------------------------
if __name__ == "__main__":
    exit(main())