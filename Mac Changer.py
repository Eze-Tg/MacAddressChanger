#!/usr/bin/env python
import subprocess
import re


def user_input():
    #Takes user's New input for interface and Mac
    global interface
    global new_mac

    interface = input("[+] * Enter name of interface: ")
    new_mac = input("[+] * Enter new MAC address: ")
    return interface, new_mac


def change_mac(interface, new_mac):
    #Uses the subprocess function and the users input from user_input function to change MAC
    print('[+] Changing MAC address for ' + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    return interface, new_mac


def get_current_mac(interface):
    #checks to confirm if User's Mac Address input is correct.
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")



user_input()
current_mac = get_current_mac(interface)

while current_mac == None:
    print("Can not find card or Mac")
    break
else:
    print("\n[+] Current MAC = ", current_mac)

result = change_mac(interface, new_mac)
newly_mac = get_current_mac(interface)
print("[+] MAC Address was successfully changed to ", newly_mac)



