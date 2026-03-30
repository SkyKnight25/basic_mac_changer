#!/usr/bin/env python

import os
import subprocess
import argparse
import re
import time

def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--interface", required=True, help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", required=True, help="New MAC address")

    return parser.parse_args()

def change_mac(interface, new_mac):
    print(f"Changing MAC address of interface \"{interface}\" to {new_mac}")

    subprocess.check_call(["ip", "link", "set", interface, "down"])
    subprocess.check_call(["ip", "link", "set", interface, "address", new_mac])
    subprocess.check_call(["ip", "link", "set", interface, "up"])

def get_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_match = re.search(r"[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}", ifconfig_result.decode())
    if mac_address_match:
        return mac_address_match.group(0)
    else:
        print("[-]MAC address not found")
        return None

if os.geteuid() != 0:
    print("[-] Please run as root")
    exit()

options = get_arguments()
change_mac(options.interface, options.mac)
time.sleep(1)
current_mac = get_mac_address(options.interface)
if current_mac.lower() == options.mac.lower():
    print(f"[+]MAC address changed successfully to {current_mac}.")
else:
    print("[-]MAC address change failed")


