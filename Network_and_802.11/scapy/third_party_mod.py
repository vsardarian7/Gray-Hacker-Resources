#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *

def nmap_simple():
    load_module("nmap")
    nmap_fp("192.168.0.114")

def os_finger():
    load_module('p0f')
    sniff(prn=prnp0f)

if __name__ == '__main__':
    nmap_simple()