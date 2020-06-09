#!/usr/bin/python3
## ping.py for  in /home/baptiste/openbsd/pinger/
## 
## Made by 
## Login   <baptiste.heraud@epitech.eu>
## 
## Started on  Fri May  6 21:02:29 2016 
## Last update Tue May 10 19:18:51 2016 
##
# -*- coding: utf-8 -*-

import sys
from function import *
import time
import socket

try:
    import logging
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from scapy.all import *
except ImportError:
    print ("this program needs scapy to work")
    sys.exit(84)

stop = False
while stop != True:
    print ("IP to ping ? ")
    ip = input()
    try:
        data = socket.gethostbyname_ex(ip)
        ip = data[2]
        stop = True
    except Exception:
        if is_ip(ip) == True:
            stop = True
        else:
            print ("invalid hostname ! check this")
ping = Ether() / IP(dst=ip) / ICMP()
while True:
    try:
        sendp(ping)
        rep_ok, rep_ko = srp(ping)
        time.sleep(1)
    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit(84)        
    except socket.error as msg:
        print ("Socket Error :%s" %msg)
        print ("You must launch this tool with rights of root")
        sys.exit(84)
