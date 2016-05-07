#!/usr/bin/python3
## ping.py for  in /home/baptiste/openbsd/pinger/
## 
## Made by 
## Login   <baptiste.heraud@epitech.eu>
## 
## Started on  Fri May  6 21:02:29 2016 
## Last update Sat May  7 09:43:48 2016 
##
# -*- coding: utf-8 -*-

import sys
from function import *
import time

try:
    import logging
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from scapy.all import *
except ImportError:
    print ("this program need scappy for work")
    sys.exit(84)

stop = False
while stop != True:
    print ("IP to ping ? ")
    ip = input()
    if is_ip(ip) == True:
      stop = True
ping = Ether() / IP(dst=ip) / ICMP()
i = 0
while i < 100000000:
    try:
        sendp(ip)
        rep_ok, rep_ko = srp(ping)
        time.sleep(1)
    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit(84)
    i = i + 1
