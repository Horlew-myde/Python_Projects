#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print("  IP\t\t\tMAC \n -----------------------------------------------------")
    client_list = []
    for packet in answered_list:
        client_dict = {"ip": packet[1].psrc, "mac address": packet[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
    print("  IP\t\t\tMAC \n -----------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac address"])


scan_result = scan("192.168.183.1/24")
print_result(scan_result)
