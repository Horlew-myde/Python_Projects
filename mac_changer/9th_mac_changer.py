#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="name of the interface to change Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="value of the Mac Address to change")
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("[+} Kindly enter a valid interface name or use --help for further directions or more information")
    elif not option.new_mac:
        parser.error("[+} Kindly enter a valid mac address or use --help for further directions or more information")
    return option

def change_mac(interface, new_mac):
    print("[+]changing MAC Address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


option = get_arguments()
change_mac(option.interface, option.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", option.interface])
print(ifconfig_result)