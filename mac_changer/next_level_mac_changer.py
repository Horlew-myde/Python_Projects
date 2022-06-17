#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "22:28:11:34:71:80"


print("[+]changing MAC Address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up ", shell=True)
