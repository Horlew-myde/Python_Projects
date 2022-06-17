#!/usr/bin/env

import scapy.all as scapy
import optparse
import argparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="TARGET IP / TARGET RANGE")
    (options, get_argument) = parser.parse_args()
    return options

# def get_argument():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-t", "--target", dest="target", help="TARGET IP / TARGET RANGE")
#     options = parser.parse_args()
#     return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "Mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC ADDRESS\n---------------------------------------------------")
    for client in results_list:
        # print(client)
        print(client["ip"] + "\t\t" + client["Mac"])

options = get_argument()
scan_result = scan(options.target)
print_result(scan_result)
