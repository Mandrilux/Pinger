#!/usr/bin/python3
## ping.py for  in /home/baptiste/rendu/test
## 
## Made by 
## Login   <baptiste@epitech.net>
## 
## Started on  Fri May  6 21:02:29 2016 
## Last update Fri May  6 21:11:21 2016 
##

# -*- coding: utf-8 -*-

import sys
try:
    import logging
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from scapy.all import *
except ImportError:
    print ("this program need scappy for work")
    sys.exit(84)

print ("put ip please")
ip = input()
ping = Ether() / IP(dst=ip) / ICMP()
i = 0
while i < 100000000:
    sendp(ip)
    i = i + 1
