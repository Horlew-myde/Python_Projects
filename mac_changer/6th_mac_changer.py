#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+]changing MAC Address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest= "interface", help="name of the interface to change Mac Address")
parser.add_option("-m", "--mac", dest="new_mac", help="value of the Mac Address to change")


(option, arguments) = parser.parse_args()

# interface = option.interface
# new_mac = option.new_mac

change_mac(option.interface, option.new_mac)
