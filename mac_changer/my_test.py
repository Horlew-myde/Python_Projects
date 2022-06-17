#!/usr/bin/env

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help=" the name of the interface you want to change")
    parser.add_option("-m", "--mac", dest="new_mac", help="the Mac Address you want to change to")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Sorry interface could not be read")
    elif not options.new_mac:
        parser.error("[+] Sorry Mac Address could not be read")
    return options
def change_mac(interface, new_mac):
    print("[+]changing Mac Address " + interface + " to : " + new_mac)
    subprocess.call(["sudo ifconfig", interface, "down"])
    subprocess.call(["sudo ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo ifconfig", interface, "up"])
def search_result(interface):
    ifconfig_result = subprocess.check_output(["sudo ifconfig", interface])
    search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if search_mac:
       return search_mac.group(0)
    else:
        print("[+]Sorry could not search Mac Address ")



options = get_arguments()
print_mac = search_result(options.interface)
print("[+]current Mac Address is" + str(print_mac))

change_mac(options.interface, options.new_mac)
print_mac = search_result(options.interface)

if print_mac == options.new_mac:
    print("[+] MAC Address was successfully changed to " + options.new_mac)
else:
    print("[-] Sanging this Shit wasn't successful my Nigga")

# interface = input()
# new_mac = input()

