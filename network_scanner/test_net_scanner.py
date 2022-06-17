#!/usr/bin/env Python
import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP / Target Router IP")
    (options, arguments) = parser.parse_args()
    return options

def scan(ip):
    scan_result = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_scan_result = broadcast/scan_result
    answered_list = scapy.srp(broadcast_scan_result, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def print_result(black_list):
    print("IP\t\t\tMAC ADDRESS\n----------------------------------------------")
    for element in black_list:
        print(element["ip"] + "\t\t" + element["mac"])


options = get_arguments()
ip_result = scan(options.target)
print_result(ip_result)