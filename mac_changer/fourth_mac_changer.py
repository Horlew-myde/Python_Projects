#!/usr/bin/env python

import subprocess

interface = input("[+] enter the interface you want to change> ")
new_mac = input("[+] enter value of the New Mac Address> ")


print("[+]changing MAC Address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up ", shell=True)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

