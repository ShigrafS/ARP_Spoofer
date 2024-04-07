# ARP_Spoofer
The arp_spoofer.py script performs an ARP spoofing attack with the help of Scapy, a Python package for packet crafting.

The ARP spoofing attack is the foundation for intercepting connections between different users on the same subnet. Basically the script is going to perform a MITM connection instead of performing an original connection. The ARP packet allows the users to identify themself on a network, computers do not understand IP addresses, and for that, every machine has an ARP table which contains the MAC addresses and their corresponded IP address for each element on the LAN.

The whole idea is send responses ("malformed packets") to the router and to the victim telling that the router is the MAC address of the attacker machine, this will change the whole data flow and the victim's traffic will be forwarded to the attacker machine.

*The Setup:*

Victim Machine (Windows 10): 192.168.1.130
Attacker Machine (Kali): 192.168.1.111
Router: 192.168.1.1 (Gateway IP)

_The Attack (ARP Spoofing):_

Victim Requests MAC Address: The victim machine sends out a request to find the MAC address of the router.
Normal ARP Response (Ignored): The actual router responds with its legitimate MAC address, but this gets ignored due to the attacker's manipulation.
Spoofed ARP Response: The attacker uses Scapy to create a fake ARP response with the router's IP address and the attacker's own MAC address. The attacker then sends this spoofed response to the victim's network.
Victim Updates ARP Table: The victim receives the spoofed response and mistakenly believes the attacker is the router. It updates its ARP table with the attacker's MAC address for the router's IP.

#Man-in-the-Middle (MITM):

Victim-Attacker Communication: Now, whenever the victim tries to communicate with the router (like accessing the internet), the traffic gets redirected to the attacker instead.
Sniffing Network Traffic: The attacker can now "sniff" the unencrypted data flowing between the victim and the attacker (pretending to be the router).

#Maintaining the Attack (Forwarding Traffic):

Denial-of-Service (DoS) Risk: By default, the attacker's machine doesn't forward traffic by itself. This disrupts the victim's internet connection and makes the attack obvious.
Enabling Packet Forwarding: The attacker needs to enable packet forwarding on their machine by setting /proc/sys/net/ipv4/ip_forward to 1. This allows the attacker to route traffic between the victim and the real router, maintaining internet access for the victim while still intercepting communication.

#Detection:

The victim can potentially discover the attack by checking their ARP table using the arp -a command.
