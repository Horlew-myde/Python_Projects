#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request. summary())
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show()
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    # print(unanswered.summary())
    print(answered.summary())



scan("10.0.2.1/24")

