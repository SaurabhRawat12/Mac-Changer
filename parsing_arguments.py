#!/usr/bin/env python


import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option('-i', '--interface', dest='interface', help='type of interface used')
parser.add_option('-m', '--mac_add', dest='mac_add', help='new mac add')
(options, arguments) = parser.parse_args()

interface = options.interface
mac_add = options.mac_add

print(f">>the  new mac address of {interface} interface is {mac_add}")
# user can pass more than one parameter in ip to reveal unwanted info
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac_add, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
