#!usr/bin/env python
import scapy.all as scapy
import optparse

# def scan(ip):
#     scapy.arping(ip)


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request.show())
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether)
    # print(broadcast.show())
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # print(arp_request_broadcast.show())
    # (answered_list, unanswered_list) = scapy.srp(arp_request_broadcast)
    answered_list = scapy.srp(arp_request_broadcast, verbose=False, timeout=1)[0]
    # print(answered_list.summary())
    print(" ip \t\t\t MAC Address \n ------------------------------------------------")
    client_list = []
    for element in answered_list:
        # print(element[1].show())
        # print("---------------------------------------------")
        # print(element[1].psrc)
        # print(element[1].hwsrc)
        # print("---------------------------------------------")
        # print(element[1].psrc + "\t\t" + element[1].hwsrc)
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    # print(client_list)
    return client_list


def print_result(result_list):
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


def get_ip():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="the ip range to scan")
    options, arguments = parser.parse_args()
    if not options.ip:
        parser.error("[+] kindly check value set/ enter value set for ip to scan")
    return options.ip


ip_value =get_ip()
scan_result = scan(ip_value)
# scan_result = scan("192.168.5.1/24")
print_result(scan_result)

# scan("192.168.5.1/24")


