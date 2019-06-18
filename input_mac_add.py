#!/usr/bin/env python3


import subprocess


interface = input("Enter the interface")

mac_add = input("Enter the mac address")

print(f">>the  new mac address of {interface} interface is {mac_add}")

# user can pass more than one parameter in ip to reveal unwanted info
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac_add, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

# user cant reveal info now
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_add])
subprocess.call(["ifconfig", interface, "up"])