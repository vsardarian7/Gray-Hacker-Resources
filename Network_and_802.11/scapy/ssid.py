#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *



def PacketHandler(pkt) :
  if pkt.haslayer(Dot11) :
        if pkt.type == 0 and pkt.subtype == 8 :
            if pkt.addr2 not in ap_list :
                ap_list.append(pkt.addr2)
                print "AP MAC: %s with SSID: %s " %(pkt.addr2, pkt.info)


if __name__ == '__main__':
    ap_list = []
    sniff(iface="wlp1s0", prn = PacketHandler)