#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="name of the interface to change Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="value of the Mac Address to change")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+} Kindly enter a valid interface name or use --help for further directions or more information")
    elif not options.new_mac:
        parser.error("[+} Kindly enter a valid mac address or use --help for further directions or more information")
    return options

def change_mac(interface, new_mac):
    print("[+]changing MAC Address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
       return mac_address_search_result.group(0)
    else:
        print("[+] sorry, could not read MAC Address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print ("[+]changed Current Mac Address to: " + str(current_mac))
# change_mac(options.interface, options.new_mac)

