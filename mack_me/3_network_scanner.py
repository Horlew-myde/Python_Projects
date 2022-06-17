#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("  IP\t\t\tMAC \n -----------------------------------------------------")
    for packet in answered_list:
        print(packet[1].psrc + "\t\t" + packet[1].hwsrc)




scan("10.0.2.1/24")

