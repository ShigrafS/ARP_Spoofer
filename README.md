# ARP_Spoofer
The arp_spoofer.py script performs an ARP spoofing attack with the help of Scapy, a Python package for packet crafting.

The ARP spoofing attack is the foundation for intercepting connections between different users on the same subnet. Basically the script is going to perform a MITM connection instead of performing an original connection. The ARP packet allows the users to identify themself on a network, computers do not understand IP addresses, and for that, every machine has an ARP table which contains the MAC addresses and their corresponded IP address for each element on the LAN.

The whole idea is send responses ("malformed packets") to the router and to the victim telling that the router is the MAC address of the attacker machine, this will change the whole data flow and the victim's traffic will be forwarded to the attacker machine.
