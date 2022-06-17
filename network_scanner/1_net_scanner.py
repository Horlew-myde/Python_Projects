#!/usr/bin/env

import scapy.all as scapy


def scan (ip):
    scapy.arping(ip)

# scan(ip [which is the ip of the router in this case, when you enter the function "route -n" on terminator])

scan("10.0.2.1/24")


