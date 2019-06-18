#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="contains the interface")
    parser.add_option("-m", "--mac_add", dest="mac_add", help="new mac address ")
    return parser.parse_args()


def change_mac(interface, mac_add):
    print(f">>the  new mac address of {interface} interface is {mac_add}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_add])
    subprocess.call(["ifconfig", interface, "up"])


(options, arguments) = get_arguments()
change_mac(options.interface, options.mac_add)


