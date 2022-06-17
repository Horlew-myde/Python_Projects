#!/usr/bin/env

import scapy.all as scapy


def scan (ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\t   MAC ADDRESS\n---------------------------------------------------")
    client_lists = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "Mac": element[1].hwsrc}
        client_lists.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
    print(client_lists)
    return client_lists


# def print_list(result_list):


scan("10.0.2.1/24")
