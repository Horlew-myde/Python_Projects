#!/usr/bin/env

import subprocess
import optparse
import re

def change_mac(interface, new_mac):
    print("[+]changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="the name of the interface you want to change")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="the Mac Address you want to change to")
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("[+]Alaye which kyn interface you enter so?")
    elif not option.new_mac:
        parser.error("[+]wetin be dis na?...... you don go press control spoil now abi")
    return option

def search_mac_address(interface):
    ifconfig_result = subprocess.check_output(["sudo", "ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return(mac_address_search_result.group(0))
    else:
        print("[+] Getat abeg, we no fit change your mac address")

option = get_arguments()
# change_mac(option.interface, option.new_mac)

current_mac = search_mac_address(option.interface)
print("[+]Current Mac Address : " + str(current_mac))

change_mac(option.interface, option.new_mac)

current_mac = search_mac_address(option.interface)

if current_mac == option.new_mac:
    print("[+] MAC Address was successfully changed to " + current_mac)
else:
    print("[-] changing this Shit wasn't successful my Nigga")
