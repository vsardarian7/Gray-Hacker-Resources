#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *

HOST ='www.google.com'

def tr():
    print traceroute(HOST)

def pi():
    print arping('192.168.1.114')

def fuzz_dns():
    send(IP(dst='192.168.1.114')/UDP()/fuzz(DNS()), inter=1,loop=1)

def fuzz_tcp():
    send(IP(dst="192.168.1.114")/fuzz(UDP()/NTP(version=4)), loop=1)

if __name__ == '__main__':
    fuzz_tcp()