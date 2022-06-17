#!/usr/bin/env python

import subprocess

interface = raw_input("interface> ")
new_mac = raw_input("New Mac> ")

# to run on python2.7 you would have to use "raw_input" instead of only "input"

print("[+]changing MAC Address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up ", shell=True)
