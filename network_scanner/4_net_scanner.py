#!/usr/bin/env

import scapy.all as scapy


def scan (ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)[0]
    # print(answered.summary())
    # print(unanswered.summary())

    print(answered.summary())

scan("10.0.2.1/24")
