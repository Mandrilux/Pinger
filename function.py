#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def is_ip(ip):
    test = ip.split('.')
    if len (test) == 4:
        try:
            nb = [int(z) for z in test]
        except ValueError:
            return False
        if nb[0] <= 255 and nb[1] <= 255 and nb[2] <= 255 and nb[3]:
            return True
        else:
            return False
    else:
        return False
