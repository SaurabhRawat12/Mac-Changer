#!/usr/bin/env python3


import subprocess
interface = "eth0"
mac_add = "00:11:22:33:44:99"

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac_add, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)