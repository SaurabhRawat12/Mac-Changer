#!/usr/bin/env python

import subprocess
import re
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="the interface u will use")
    parser.add_option("-m", "--mac_add", dest="mac_add", help="the mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please check the interface entered, type --help for more info")
    elif not options.mac_add:
        parser.error("[-] please check the mac_address entered, type --help for more info")
    return options


def change_mac(interface, mac_add):
    print(f">>the  new mac address of {interface} interface is {mac_add}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_add])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode()
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("Sorry no result")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("current Mac : " + str(current_mac))
change_mac(options.interface, options.mac_add)
current_mac = get_current_mac(options.interface)
if current_mac == options.mac_add:
    print("MAC Address change to :" + current_mac)
else:
    print("sorry didnt changed")
