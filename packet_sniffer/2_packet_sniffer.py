#!/usr/bin/env Python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

    # scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter=)
    # filters eg is "udp": for phonecalls, images, videos etc, arp,tcp, port 21. port 80

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet.show())


sniff("usb0")
