#!/usr/bin/env python

# python3 main.py -i <interface name> -m <new MAC address>

import subprocess
import optparse

original_mac = "00:0c:29:5b:7e:43"

def change_mac(interface, new_mac):
    ### Easy Code , Risk with Command Hijack ###
    # subprocess.call(f"sudo ifconfig {interface} down", shell=True)
    # subprocess.call(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
    # subprocess.call(f"sudo ifconfig {interface} up", shell=True)
    # subprocess.call(f"sudo ifconfig", shell=True)

    #### Secure Code, Avoid Code Hijack #####
    print(f"[+] Changing MAC address for {interface} interface to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()


change_mac(options.interface, options.new_mac)

