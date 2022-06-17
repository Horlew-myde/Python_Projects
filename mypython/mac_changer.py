#!usr/bin/env python
import subprocess
import optparse
import re


def change_mac(iface, new_mac):
    print("[+]Changing Current MAC Address of " + iface + "to " + new_mac)
    subprocess.call(["sudo", "ifconfig", iface, "down"])
    subprocess.call(["sudo", "ifconfig", iface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", iface, "up"])


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="iface", help="the name of the interface to change")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    options, arguments = parser.parse_args()
    if not options.iface:
        parser.error("[+] kindly check value set/ enter value set for interface")
    elif not options.new_mac:
        parser.error("[+] kindly check value set / enter value for MAC Address")
    return options


def check_mac(iface):
    ifconfig_result = subprocess.check_output(["sudo", "ifconfig", options.iface])
    search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if search_result:
        return search_result.group(0)
    else:
        print("could not change Mac Address")


# iface = input("interface : ")
# new_mac = input("MAC : ")

options = get_argument()
current_mac = check_mac(options.iface)
print("[+] Current Mac : " + str(current_mac))
change_mac(options.iface, options.new_mac)
changed_mac = check_mac(options.iface)
if current_mac == changed_mac:
    print("[+] Mac Address Not Changed!!!!!")
else:
    print("[+]MAC Address was Successfully Changed to : " + str(current_mac))



