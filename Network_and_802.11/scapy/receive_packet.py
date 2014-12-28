#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *

def sr_simple():
    output=sr(IP(dst='google.com')/ICMP())
    print '\nOutput is:'
    print output
    result, unanswered=output
    print '\nResult is:'
    print result[0]


def srloop_simple():
    srloop(IP(dst="www.google.com")/ICMP(), count=3)

if __name__ == '__main__':
    srloop_simple